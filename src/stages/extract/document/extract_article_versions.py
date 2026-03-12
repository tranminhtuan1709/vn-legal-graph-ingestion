from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract


def fetch_article_versions(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    try:
        cursor.execute(
            operation="""
                WITH article_versions AS (
                    SELECT
                        core_noidungsuadoi.id AS version_id,
                        
                        core_noidungsuadoi.vbplsd_id AS from_vbpl_id,
                        core_noidungsuadoi.dieu AS from_article_number,
                        core_noidungsuadoi.phu_luc AS from_appendix_number,
                        
                        core_reviewdieuluat.vbpldsd_id AS to_vbpl_id,
                        core_reviewdieuluat.dieu AS to_article_number,
                        core_reviewdieuluat.phu_luc AS to_appendix_number,
                        
                        core_reviewdieuluat.loai_vb AS modification_type,
                        core_noidungsuadoi.noi_dung_sua_doi AS modification_content,
                        core_noidungsuadoi.bai_bo_noi_dung_truoc AS is_abolish_previous_content,
                        core_noidungsuadoi.from_date,
                        core_noidungsuadoi.to_date
                    FROM core_reviewdieuluat
                    JOIN core_noidungsuadoi
                    ON core_reviewdieuluat.id = core_noidungsuadoi.review_dieu_luat_id
                    WHERE core_reviewdieuluat.vbpldsd_id = %(document_id)s

                    UNION ALL
                    
                    SELECT
                        core_noidungsuadoi.id AS version_id,
                    
                        core_noidungsuadoi.vbplsd_id AS from_vbpl_id,
                        core_noidungsuadoi.dieu AS from_article_number,
                        core_noidungsuadoi.phu_luc AS from_appendix_number,
                        
                        core_reviewdieuluat.vbpldsd_id AS to_vbpl_id,
                        core_reviewdieuluat.dieu AS to_article_number,
                        core_reviewdieuluat.phu_luc AS to_appendix_number,
                        
                        core_reviewdieuluat.loai_vb AS modification_type,
                        core_noidungsuadoi.noi_dung_sua_doi AS modification_content,
                        core_noidungsuadoi.bai_bo_noi_dung_truoc AS is_abolish_previous_content,
                        core_noidungsuadoi.from_date,
                        core_noidungsuadoi.to_date
                    FROM core_reviewdieuluat
                    JOIN core_noidungsuadoi 
                    ON core_reviewdieuluat.id = core_noidungsuadoi.review_dieu_luat_id
                    WHERE core_noidungsuadoi.vbplsd_id = %(document_id)s
                )
                SELECT
                    article_versions.version_id,
                    
                    vs1.id AS from_article_id,
                    article_versions.from_article_number,
                    vs1.section_name AS from_article_name,
                    vs1.section_content AS from_article_content,
                    article_versions.from_appendix_number,
                    DATE(vs1.effective_date) AS from_effective_date,
                    
                    vs2.id AS to_article_id,
                    article_versions.to_article_number,
                    vs2.section_name AS to_article_name,
                    vs2.section_content AS to_article_content,
                    article_versions.to_appendix_number,
                    DATE(vs2.effective_date) AS to_effective_date,
                    
                    article_versions.modification_type,
                    article_versions.modification_content,
                    article_versions.is_abolish_previous_content,
                    DATE(article_versions.from_date) AS from_date,
                    DATE(article_versions.to_date) AS from_date
                FROM article_versions
                JOIN vbpl_section AS vs1
                ON
                    article_versions.from_vbpl_id = vs1.vbpl_id AND
                    NULLIF(article_versions.from_article_number, '') COLLATE utf8mb4_general_ci
                        <=> NULLIF(vs1.section_number, '') COLLATE utf8mb4_general_ci AND
                    NULLIF(article_versions.from_appendix_number, '') COLLATE utf8mb4_general_ci 
                        <=> NULLIF(vs1.so_phu_luc, '') COLLATE utf8mb4_general_ci
                JOIN vbpl_section AS vs2
                ON
                    article_versions.to_vbpl_id = vs2.vbpl_id AND
                    NULLIF(article_versions.to_article_number, '') COLLATE utf8mb4_general_ci 
                        = NULLIF(vs2.section_number, '') COLLATE utf8mb4_general_ci AND
                    NULLIF(article_versions.to_appendix_number, '') COLLATE utf8mb4_general_ci 
                        <=> NULLIF(vs2.so_phu_luc, '') COLLATE utf8mb4_general_ci
                ORDER BY article_versions.from_date
            """,
            params={
                "document_id": document_id
            }
        )

        records = cursor.fetchall()

        for record in records:
            record["is_abolish_previous_content"] = bool(record["is_abolish_previous_content"])

        return records
    except Exception:
        raise
