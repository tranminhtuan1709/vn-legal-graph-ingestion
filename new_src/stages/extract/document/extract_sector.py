import time
from mysql.connector.abstracts import MySQLCursorAbstract

from dtos.extracted.document.extracted_sector import ExtractedSector
from utils.logger import logger

def fetch_sector(cursor: MySQLCursorAbstract, sector_id: int) -> ExtractedSector:
    start_time = time.time()

    try:
        cursor.execute(
            operation="""
                SELECT
                    id,
                    linh_vuc
                FROM vbpl_sector
                WHERE id = %(sector_id)s;
            """,
            params={
                "sector_id": sector_id
            }
        )

        record = cursor.fetchone()

        return ExtractedSector(**record)
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
    