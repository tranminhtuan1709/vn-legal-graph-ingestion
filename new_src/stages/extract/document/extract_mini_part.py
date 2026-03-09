import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_mini_part import ExtractedMiniPart
from utils.logger import logger


def fetch_mini_parts(cursor: MySQLCursorAbstract, document_id: int) -> list[ExtractedMiniPart]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    vbpl_id,
                    vbpl_part_id,
                    big_part_number,
                    big_part_name
                FROM vbpl_mini_part
                WHERE vbpl_id = %(document_id)s
            """,
            params={
                "document_id": document_id
            }
        )

        records = cursor.fetchall()

        return [ExtractedMiniPart(**record) for record in records]
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    