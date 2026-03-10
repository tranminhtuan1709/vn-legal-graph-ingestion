import time
from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract

from utils.logger import logger


def fetch_big_parts(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    vbpl_id,
                    big_part_number,
                    big_part_name
                FROM vbpl_big_part
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
    