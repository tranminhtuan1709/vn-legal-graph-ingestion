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
    
    def create_nodes(self, nodes: list[Node]) -> None:
        if nodes == []:
            return
        
        session = self.neo4j_client.get_session()

        try:
            transaction = session.begin_transaction()
        except Exception as e:
            raise InfrastructureError(message="Failed to create transaction from a Neo4j session") from e

        try:
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
        except Exception as e:
            transaction.rollback()
            raise CreateNodeError(message="Failed to create nodes") from e
        finally:
            transaction.close()
            session.close()
    
    def create_edges(self, triples: list[Triple]) -> None:
        if triples == []:
            return
        
        session = self.neo4j_client.get_session()

        try:
            transaction = session.begin_transaction()
        except Exception as e:
            raise InfrastructureError(message="Failed to create transaction from a Neo4j session") from e
        
        try:
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
