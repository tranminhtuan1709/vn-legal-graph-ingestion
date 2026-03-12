from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract


def fetch_chapters(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    try:
        cursor.execute(
            operation="""
                SELECT
                    vbpl_id AS document_id,
                    vbpl_big_part_id AS big_part_id,
                    id AS chapter_id,
                    chapter_number,
                    chapter_name
                FROM vbpl_chapter
                WHERE vbpl_id = %(document_id)s
            """,
            params={
                "document_id": document_id
            }
        )

        return cursor.fetchall()
    except Exception:
        raise
