import time
from mysql.connector.abstracts import MySQLCursorAbstract
from typing import Any

from utils.logger import logger

def fetch_document(cursor: MySQLCursorAbstract, document_id: int) -> dict[str, Any]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id AS document_id,
                    so_ky_hieu AS document_number,
                    ten_vbpl AS document_name,
                    DATE(ngay_ban_hanh) AS issued_date,
                    DATE(ngay_co_hieu_luc) AS effective_date,
                    DATE(ngay_het_han) AS expiry_date,
                    trang_thai AS status,
                    chu_thich_nho AS small_note,
                    loai_van_ban AS document_type,
                    linh_vuc AS sector,
                    co_quan_ban_hanh AS issuing_authorities,
                    id_loai_van_ban AS document_type_id,
                    id_linh_vuc AS sector_id,
                    id_co_quan_ban_hanh AS issuing_authority_ids
                FROM vbpl
                WHERE id = %(document_id)s;
            """,
            params={
                "document_id": document_id
            }
        )

        return cursor.fetchone()
    except Exception:
        raise
    finally:
        logger.info(f"{time.time() - start_time} s")
    