from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract


def fetch_parts(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    try:
        cursor.execute(
            operation="""
                SELECT
                    vbpl_id AS document_id,
                    vbpl_chapter_id AS chapter_id,
                    id AS part_id,
                    part_number,
                    part_name
                FROM vbpl_part
                WHERE vbpl_id = %(document_id)s
            """,
            params={
                "document_id": document_id
            }
        )

        return cursor.fetchall()
    except Exception:
        raise
