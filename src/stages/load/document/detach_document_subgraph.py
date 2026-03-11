import time
from neo4j import Transaction

from utils.logger import logger
from utils.uuid_utils import get_node_id


def detach_document_subgraph(transaction: Transaction, document_id: str) -> None:
    start_time = time.time()

    try:    
        transaction.run(
            query="""
                MATCH (root:Document {node_id: $node_id})
                OPTIONAL MATCH (root)-[:CONTAIN|IS_AMENDED_TO *1..]->(child)
                WITH DISTINCT root, child
                DETACH DELETE root, child
            """,
            parameters={
                "node_id": get_node_id(business_id=document_id, node_label="Document")
            }
        )
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    