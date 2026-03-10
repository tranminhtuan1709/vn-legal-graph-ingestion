import time
from neo4j import Transaction

from dtos.graph.edges.edge import Edge
from utils.logger import logger


def create_edges(transaction: Transaction, edges: list[Edge]) -> None:
    for edge in edges:
        print(edge.__dict__)
    
    start_time = time.time()
    
    try:
        if edges == []:
            return
        
        edge_groups: dict[str, list[Edge]] = {}

        for edge in edges:
            if edge.edge_type not in edge_groups:
                edge_groups[edge.edge_type] = [edge]
            else:
                edge_groups[edge.edge_type].append(edge)
        
        for group_type, group_edges in edge_groups.items():
            batch = []

            for edge in group_edges:
                batch.append(
                    {
                        "from_node_id": edge.from_node_id,
                        "to_node_id": edge.to_node_id,
                        "edge_properties": edge.model_dump(exclude={"from_node_id", "to_node_id"})
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
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    