import time
from typing import Any

from infrastructure.mysql_client import MySQLClient
from infrastructure.neo4j_client import Neo4jClient

from stages.extract.document.extract_document import fetch_document
from stages.extract.document.extract_big_part import fetch_big_parts
from stages.extract.document.extract_chapter import fetch_chapters
from stages.extract.document.extract_part import fetch_parts
from stages.extract.document.extract_mini_part import fetch_mini_parts
from stages.extract.document.extract_article import fetch_articles
from stages.extract.document.extract_article_version import fetch_article_versions
from stages.extract.document.extract_document_mapping import fetch_document_mappings

from stages.transform.document.transform_document_dto import transform_document_dto
from stages.transform.document.transform_big_part_dto import transform_big_part_dtos
from stages.transform.document.transform_chapter_dto import transform_chapter_dtos
from stages.transform.document.transform_part_dto import transform_part_dtos
from stages.transform.document.transform_mini_part_dto import transform_mini_part_dtos
from stages.transform.document.transform_article_dto import transform_article_dtos
from stages.transform.document.transform_article_version import transform_article_version_dtos
from stages.transform.document.transform_document_mapping import transform_document_mapping_dtos
from stages.transform.document.document_to_graph import document_to_graph

from stages.load.create_node import create_nodes
from stages.load.create_edge import create_edges
from stages.load.document.detach_document_subgraph import detach_document_subgraph

from dtos.document.document_data import DocumentData
from dtos.graph.nodes.node import Node
from dtos.graph.edges.edge import Edge

from utils.logger import logger


class DocumentPipeline:
    def __init__(self, mysql_client: MySQLClient, neo4j_client: Neo4jClient) -> None:
        self.mysql_client = mysql_client
        self.neo4j_client = neo4j_client

    def extract(self, document_id: int) -> dict[str, Any]:
        start_time = time.time()
        connection = None
        cursor = None

        try:
            connection = self.mysql_client.get_connection()
            cursor = connection.cursor(dictionary=True)

            return {
                "document": fetch_document(cursor, document_id),
                "big_parts": fetch_big_parts(cursor, document_id),
                "chapter": fetch_chapters(cursor, document_id),
                "parts": fetch_parts(cursor, document_id),
                "mini_parts": fetch_mini_parts(cursor, document_id),
                "articles": fetch_articles(cursor, document_id),
                "article_versions": fetch_article_versions(cursor, document_id),
                "document_mappings": fetch_document_mappings(cursor, document_id)
            }
        except Exception:
            raise
        finally:
            logger.info(f"{time.time() - start_time} s")

            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()
    
    def transform(self, raw_data: dict[str, Any]) -> tuple[list[Node], list[Edge]]:
        start_time = time.time()

        try:
            document_data =  DocumentData(
                transform_document_dto(raw_data.get("document")),
                transform_big_part_dtos(raw_data.get("big_parts")),
                transform_chapter_dtos(raw_data.get("chapters")),
                transform_part_dtos(raw_data.get("parts")),
                transform_mini_part_dtos(raw_data.get("mini_parts")),
                transform_article_dtos(raw_data.get("articles")),
                transform_article_version_dtos(raw_data.get("article_versions")),
                transform_document_mapping_dtos(raw_data.get("document_mappings"))
            )
            
            return document_to_graph(document_data)
        except Exception:
            raise
        finally:
            logger.info(f"{time.time() - start_time} s")
    
    def load(self, document_id: int, nodes: list[Node], edges: list[Edge]) -> None:
        start_time = time.time()
        session = None
        transaction = None

        try:
            session = self.neo4j_client.get_session()
            transaction = session.begin_transaction()
            

            detach_document_subgraph(transaction, document_id)
            create_nodes(transaction, nodes)
            create_edges(transaction, edges)
        except Exception:
            if transaction is not None:
                transaction.rollback()
            
            raise
        finally:
            logger.info(f"{time.time() - start_time} s")

            if transaction is not None:
                transaction.close()

            if session is not None:
                session.close()

    
    def run(self, document_id: int) -> None:
        start_time = time.time()

        try:
            raw_data = self.extract(document_id)
            nodes, edges = self.transform(raw_data)
            self.load(document_id, document_id, nodes, edges)
            logger.info(f"Processed document ID {document_id}")
        except Exception:
            logger.error(f"Failed while processing document ID: {document_id}", exc_info=True)
        finally:
            logger.info(f"{time.time() - start_time} s")
            logger.info(f"{'=' * 100}\n\n\n")
    