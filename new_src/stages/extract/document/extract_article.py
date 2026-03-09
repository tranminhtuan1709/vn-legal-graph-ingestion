import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_article import ExtractedArticle
from utils.logger import logger


def fetch_articles(cursor: MySQLCursorAbstract, document_id: int) -> list[ExtractedArticle]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    vbpl_id,
                    vbpl_big_part_id,
                    vbpl_chapter_id,
                    vbpl_part_id,
                    vbpl_mini_part_id,
                    section_number,
                    section_name,
                    section_content,
                    so_phu_luc,
                    effective_date
                FROM vbpl_section
                WHERE vbpl_id = %(document_id)s
            """,
            params={
                "document_id": document_id
            }
        )

        records = cursor.fetchall()

        return [ExtractedArticle(**record) for record in records]
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    