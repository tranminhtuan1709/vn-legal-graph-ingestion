import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_document import ExtractedDocument
from utils.logger import logger

def fetch_document(cursor: MySQLCursorAbstract, document_id: int) -> ExtractedDocument:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    so_ky_hieu,
                    ten_hien_thi,
                    ngay_ban_hanh,
                    ngay_co_hieu_luc,
                    ngay_het_han,
                    trang_thai,
                    chu_thich_nho,
                    loai_van_ban,
                    linh_vuc,
                    co_quan_ban_hanh,
                    id_loai_van_ban,
                    id_linh_vuc,
                    id_co_quan_ban_hanh
                FROM vbpl
                WHERE id = %(document_id)s;
            """,
            params={
                "document_id": document_id
            }
        )

        record = cursor.fetchone()

        return ExtractedDocument(**record)
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    