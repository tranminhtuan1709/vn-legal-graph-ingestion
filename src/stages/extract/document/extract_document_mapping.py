from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract


def fetch_document_mappings(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    try:
        cursor.execute(
            operation="""
                SELECT
                    vbpl_doc_map.id AS mapping_id,
                    vbpl_doc_map.relationship_type,

                    vbpl_doc_map.from_document_id,
                    vbpl1.so_ky_hieu AS from_document_number,
                    vbpl1.ten_hien_thi AS from_document_name,
                    DATE(vbpl1.ngay_ban_hanh) AS from_issued_date,
                    DATE(vbpl1.ngay_co_hieu_luc) AS from_effective_date,
                    DATE(vbpl1.ngay_het_han) AS from_expiry_date,
                    vbpl1.trang_thai AS from_status,
                    vbpl1.chu_thich_nho AS from_small_note,
                    
                    vbpl_doc_map.to_document_id,
                    vbpl2.so_ky_hieu AS to_document_number,
                    vbpl2.ten_hien_thi AS to_document_name,
                    DATE(vbpl2.ngay_ban_hanh) AS to_issued_date,
                    DATE(vbpl2.ngay_co_hieu_luc) AS to_effective_date,
                    DATE(vbpl2.ngay_het_han) AS to_expiry_date,
                    vbpl2.trang_thai AS to_status,
                    vbpl2.chu_thich_nho AS to_small_note
                FROM vbpl_doc_map
                JOIN vbpl AS vbpl1 ON vbpl_doc_map.from_document_id = vbpl1.id
                JOIN vbpl AS vbpl2 ON vbpl_doc_map.to_document_id = vbpl2.id
                WHERE
                    vbpl_doc_map.from_document_id = %(document_id)s OR
                    vbpl_doc_map.to_document_id = %(document_id)s
            """,
            params={
                "document_id": document_id
            }
        )

        return cursor.fetchall()
    except Exception:
        raise
