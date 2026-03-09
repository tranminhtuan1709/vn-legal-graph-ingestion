import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_issuing_authority import ExtractedIssuingAuthority
from utils.logger import logger


def fetch_issuing_authorities(
    cursor: MySQLCursorAbstract,
    issuing_authority_ids: list[int]
) -> list[ExtractedIssuingAuthority]:
    start_time = time.time()

    try:
        if issuing_authority_ids == []:
            return []
        
        placeholders = ",".join(["%s"] * len(issuing_authority_ids))

        cursor.execute(
            operation=f"""
                SELECT
                    id,
                    co_quan_ban_hanh
                FROM vbpl_issuing_authority
                WHERE id IN ({placeholders})
            """,
            params=tuple(issuing_authority_ids)
        )

        records = cursor.fetchall()

        return [ExtractedIssuingAuthority(**record) for record in records]
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    