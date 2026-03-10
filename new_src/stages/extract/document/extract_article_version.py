import time
from typing import Any
from mysql.connector.abstracts import MySQLCursorAbstract

from utils.logger import logger


def fetch_article_versions(cursor: MySQLCursorAbstract, document_id: int) -> list[dict[str, Any]]:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                WITH article_versions AS (
                    SELECT
                        core_noidungsuadoi.id AS version_id,
                        core_noidungsuadoi.vbplsd_id,
                        core_reviewdieuluat.vbpldsd_id,
                        core_noidungsuadoi.dieu AS dieu_sd,
                        core_reviewdieuluat.dieu AS dieu_dsd,
                        core_noidungsuadoi.phu_luc AS phu_luc_sd,
                        core_reviewdieuluat.phu_luc AS phu_luc_dsd,
                        core_reviewdieuluat.loai_vb,
                        core_noidungsuadoi.bai_bo_noi_dung_truoc,
                        core_noidungsuadoi.noi_dung_sua_doi,
                        core_noidungsuadoi.from_date,
                        core_noidungsuadoi.to_date
                    FROM core_reviewdieuluat
                    JOIN core_noidungsuadoi 
                    ON core_reviewdieuluat.id = core_noidungsuadoi.review_dieu_luat_id
                    WHERE core_reviewdieuluat.vbpldsd_id = %(document_id)s

                    UNION ALL

                    SELECT
                        core_noidungsuadoi.id AS version_id,
                        core_noidungsuadoi.vbplsd_id,
                        core_reviewdieuluat.vbpldsd_id,
                        core_noidungsuadoi.dieu AS dieu_sd,
                        core_reviewdieuluat.dieu AS dieu_dsd,
                        core_noidungsuadoi.phu_luc AS phu_luc_sd,
                        core_reviewdieuluat.phu_luc AS phu_luc_dsd,
                        core_reviewdieuluat.loai_vb,
                        core_noidungsuadoi.bai_bo_noi_dung_truoc,
                        core_noidungsuadoi.noi_dung_sua_doi,
                        core_noidungsuadoi.from_date,
                        core_noidungsuadoi.to_date
                    FROM core_reviewdieuluat
                    JOIN core_noidungsuadoi 
                    ON core_reviewdieuluat.id = core_noidungsuadoi.review_dieu_luat_id
                    WHERE core_noidungsuadoi.vbplsd_id = %(document_id)s
                )
                SELECT
                    article_versions.version_id,
                    article_versions.vbplsd_id,
                    article_versions.vbpldsd_id,
                    article_versions.dieu_sd,
                    article_versions.dieu_dsd,
                    vs1.id AS dieu_sd_id,
                    vs2.id AS dieu_dsd_id,
                    article_versions.phu_luc_sd,
                    article_versions.phu_luc_dsd,
                    article_versions.loai_vb,
                    CONVERT(article_versions.from_date, CHAR) AS from_date,
                    CONVERT(article_versions.to_date, CHAR) AS to_date,
                    article_versions.bai_bo_noi_dung_truoc,
                    article_versions.noi_dung_sua_doi
                FROM article_versions
                JOIN vbpl_section AS vs1
                ON
                    article_versions.vbplsd_id = vs1.vbpl_id AND
                    NULLIF(article_versions.dieu_sd, '') COLLATE utf8mb4_general_ci
                        <=> NULLIF(vs1.section_number, '') COLLATE utf8mb4_general_ci AND
                    NULLIF(article_versions.phu_luc_sd, '') COLLATE utf8mb4_general_ci 
                        <=> NULLIF(vs1.so_phu_luc, '') COLLATE utf8mb4_general_ci
                JOIN vbpl_section AS vs2
                ON
                    article_versions.vbpldsd_id = vs2.vbpl_id AND
                    NULLIF(article_versions.dieu_dsd, '') COLLATE utf8mb4_general_ci 
                        = NULLIF(vs2.section_number, '') COLLATE utf8mb4_general_ci AND
                    NULLIF(article_versions.phu_luc_dsd, '') COLLATE utf8mb4_general_ci 
                        <=> NULLIF(vs2.so_phu_luc, '') COLLATE utf8mb4_general_ci
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
    