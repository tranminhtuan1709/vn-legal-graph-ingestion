import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_chapter import ExtractedChapter
from utils.logger import logger


def fetch_chapters(cursor: MySQLCursorAbstract, document_id: int) -> list[ExtractedChapter]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    vbpl_id,
                    vbpl_big_part_id,
                    chapter_number,
                    chapter_name
                FROM vbpl_chapter
                WHERE vbpl_id = %(document_id)s
            """,
            params={
                "document_id": document_id
            }
        )

        records = cursor.fetchall()

        return [ExtractedChapter(**record) for record in records]
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    