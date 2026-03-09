import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_document_type import ExtractedDocumentType
from utils.logger import logger

def fetch_document_type(cursor: MySQLCursorAbstract, document_type_id: int) -> ExtractedDocumentType:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    loai_van_ban
                FROM vbpl_doc_type
                WHERE id = %(document_type_id)s;
            """,
            params={
                "document_type_id": document_type_id
            }
        )

        record = cursor.fetchone()

        return ExtractedDocumentType(**record)
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    