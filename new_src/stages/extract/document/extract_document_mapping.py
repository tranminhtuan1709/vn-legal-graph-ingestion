import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_document_mapping import ExtractedDocumentMapping
from utils.logger import logger


def fetch_document_mappings(cursor: MySQLCursorAbstract, document_id: int) -> list[ExtractedDocumentMapping]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    from_document_id,
                    to_document_id,
                    relationship_type
                FROM vbpl_doc_map
                WHERE
                    from_document_id = %(document_id)s OR
                    to_document_id = %(document_id)s
            """,
            params={
                "document_id": document_id
            }
        )

        records = cursor.fetchall()

        return [ExtractedDocumentMapping(**record) for record in records]
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    