import time
from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract

from utils.logger import logger


def fetch_document_mappings(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    from_document_id,
                    to_document_id,
                    relationship_type
                FROM vbpl_doc_map
                WHERE
                    from_document_id = %(document_id)s OR
                    to_document_id = %(document_id)s
            """,
            params={
                "document_id": document_id
            }
        )

        return cursor.fetchall()
    except Exception:
        raise
    finally:
        logger.info(f"{time.time() - start_time} s")
    