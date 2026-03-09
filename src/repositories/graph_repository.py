import time

from interface.dtos.internal.graph.node import Node
from interface.dtos.internal.graph.triple import Triple
from infrastructure.neo4j_client import Neo4jClient

from utils.logger import logger


class GraphRepository:
    def __init__(self, neo4j_client: Neo4jClient) -> None:
        self.neo4j_client = neo4j_client
    
    def create_nodes(self, nodes: list[Node]) -> None:
        start_time = time.time()

        try:
            if nodes == []:
                return
            
            session = self.neo4j_client.get_session()
            transaction = session.begin_transaction()

            node_groups: dict[str, list[Node]] = {}

            for node in nodes:
                if node.node_label not in node_groups:
                    node_groups[node.node_label] = [node]
                else:
                    node_groups[node.node_label].append(node)
            
            for group_label, group_nodes in node_groups.items():
                batch = [node.__dict__ for node in group_nodes]

                transaction.run(
                    query=f"""
                    UNWIND $batch AS row
                    MERGE (node:{group_label} {{node_id: row.node_id}})
                    SET node += row
                    """,
                    parameters={
                        "batch": batch,
                    }
                )

            transaction.commit() 
        except Exception:
            transaction.rollback()
            raise
        finally:
            transaction.close()
            session.close()
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
    
    def create_edges(self, triples: list[Triple]) -> None:
        start_time = time.time()
        
        try:
            if triples == []:
                return
            
            session = self.neo4j_client.get_session()
            transaction = session.begin_transaction()

            edge_groups: dict[str, list[Triple]] = {}

            for triple in triples:
                if triple.edge.edge_type not in edge_groups:
                    edge_groups[triple.edge.edge_type] = [triple]
                else:
                    edge_groups[triple.edge.edge_type].append(triple)
            
            for group_type, group_triples in edge_groups.items():
                batch = []

                for triple in group_triples:
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
                        MERGE (from_node)-[edge:{group_type}]->(to_node)
                        SET edge += row.edge_properties
                    """,
                    parameters={
                        "batch": batch
                    }
                )
            transaction.commit()
        except Exception:
            transaction.rollback()
            raise
        finally:
            transaction.close()
            session.close()
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
    
    def detach_document_subgraph(self, node_id: str) -> None:
        start_time = time.time()

        try:
            session = self.neo4j_client.get_session()
            transaction = session.begin_transaction()
        
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
            raise
        finally:
            transaction.close()
            session.close()
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
