import time
from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract

from utils.logger import logger


def fetch_mini_parts(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    vbpl_id AS document_id,
                    vbpl_part_id AS part_id,
                    id AS mini_part_id,
                    mini_part_number,
                    mini_part_name
                FROM vbpl_mini_part
                WHERE vbpl_id = %(document_id)s
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
    