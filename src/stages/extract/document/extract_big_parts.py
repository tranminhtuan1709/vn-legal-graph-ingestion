from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract


def fetch_big_parts(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    try:
        cursor.execute(
            operation="""
                SELECT
                    vbpl_id AS document_id,
                    id AS big_part_id,
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
