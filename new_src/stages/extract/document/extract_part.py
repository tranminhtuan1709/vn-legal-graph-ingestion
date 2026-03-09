import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_part import ExtractedPart
from utils.logger import logger


def fetch_parts(cursor: MySQLCursorAbstract, document_id: int) -> list[ExtractedPart]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    vbpl_id,
                    vbpl_chapter_id
                    part_number,
                    part_name
                FROM vbpl_part
                WHERE vbpl_id = %(document_id)s
            """,
            params={
                "document_id": document_id
            }
        )

        records = cursor.fetchall()

        return [ExtractedPart(**record) for record in records]
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    