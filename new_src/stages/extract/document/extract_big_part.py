import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_big_part import ExtractedBigPart
from utils.logger import logger


def fetch_big_parts(cursor: MySQLCursorAbstract, document_id: int) -> list[ExtractedBigPart]:
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

        records = cursor.fetchall()

        return [ExtractedBigPart(**record) for record in records]
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    