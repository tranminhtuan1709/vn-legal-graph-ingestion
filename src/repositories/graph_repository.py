from src.interface.dtos.internal.graph.node import Node
from src.interface.dtos.internal.graph.triple import Triple
from src.infrastructure.neo4j_client import Neo4jClient

from src.exceptions.custom_exceptions import (
    InfrastructureError,
    CreateNodeError,
    CreateEdgeError,
    DetachSubgraphError
)


class GraphRepository:
    def __init__(self, neo4j_client: Neo4jClient) -> None:
        self.neo4j_client = neo4j_client
    
    def create_nodes(self, node_label: str, nodes: list[Node]) -> None:
        if nodes == []:
            return
        
        session = self.neo4j_client.get_session()

        try:
            transaction = session.begin_transaction()
        except Exception as e:
            raise InfrastructureError(message="Failed to create transaction from a Neo4j session") from e

        try:
            batch = [node.__dict__ for node in nodes]

            transaction.run(
                query=f"""
                UNWIND $batch AS row
                CREATE (node:{node_label})
                SET node = row
                """,
                parameters={
                    "batch": batch,
                }
            )

            transaction.commit()
        except Exception as e:
            transaction.rollback()
            raise CreateNodeError(message="Failed to create nodes") from e
        finally:
            transaction.close()
            session.close()
    
    def create_edges(self, edge_type: str, triples: list[Triple]) -> None:
        if triples == []:
            return
        
        session = self.neo4j_client.get_session()

        try:
            transaction = session.begin_transaction()
        except Exception as e:
            raise InfrastructureError(message="Failed to create transaction from a Neo4j session") from e
        
        try:
            batch = []

            for triple in triples:
                batch.append(
                    {
                        "from_node_id": triple.from_node_id,
                        "to_node_id": triple.to_node_id,
                        "edge_properties": triple.edge.__dict__
                    }
                )
            
            transaction.run(
                query=f"""
                    UNWIND $batch AS row
                    MATCH (from_node {{node_id: row.from_node_id}})
                    MATCH (to_node {{node_id: row.to_node_id}})
                    CREATE (from_node)-[edge:{edge_type}]->(to_node)
                    SET edge = row.edge_properties
                """,
                parameters={
                    "batch": batch
                }
            )

            transaction.commit()
        except Exception as e:
            transaction.rollback()
            raise CreateEdgeError(message="Failed to create edges") from e
        finally:
            transaction.close()
            session.close()
    
    def detach_document_subgraph(self, node_id: str) -> None:
        session = self.neo4j_client.get_session()

        try:
            transaction = session.begin_transaction()
        except Exception as e:
            raise InfrastructureError(message="Failed to create transaction from a Neo4j session") from e
        
        try:
            transaction.run(
                query="""
                    MATCH (root:Document {node_id: $node_id})
                    OPTIONAL MATCH (root)-[:CONTAIN|IS_AMENDED_TO *1..]->(child)
                    WITH DISTINCT root, child
                    DETACH DELETE root, child
                """,
                parameters={
                    "node_id": node_id
                }
            )

            transaction.commit()
        except Exception as e:
            transaction.rollback()

            raise DetachSubgraphError(
                message=f"Failed to detach a document subgraph",
                context={
                    "document_id": node_id
                }
            ) from e
        finally:
            transaction.close()
            session.close()
