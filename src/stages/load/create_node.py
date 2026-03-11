import time
from neo4j import Transaction

from dtos.graph.nodes.node import Node
from utils.logger import logger


def create_nodes(transaction: Transaction, nodes: list[Node]) -> None:
    start_time = time.time()

    try:
        if nodes == []:
            return
        
        node_groups: dict[str, list[Node]] = {}

        for node in nodes:
            if node.node_label not in node_groups:
                node_groups[node.node_label] = [node]
            else:
                node_groups[node.node_label].append(node)
        
        for group_label, group_nodes in node_groups.items():
            batch = [node.model_dump_json(exclude={"node_label"}) for node in group_nodes]

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
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    