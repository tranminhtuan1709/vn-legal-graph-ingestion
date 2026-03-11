import time
from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract

from utils.logger import logger


def fetch_articles(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    vbpl_id AS document_id,
                    vbpl_big_part_id AS big_part_id,
                    vbpl_chapter_id AS chapter_id,
                    vbpl_part_id AS part_id,
                    vbpl_mini_part_id AS mini_part_id,
                    id AS article_id,
                    section_number AS article_number,
                    section_name AS article_name,
                    section_content AS article_content,
                    so_phu_luc AS appendix,
                    DATE(effective_date) AS effective_date
                FROM vbpl_section
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
    