import time
import json
from mysql.connector.abstracts import MySQLCursorAbstract, MySQLConnectionAbstract

from dtos.extracted.document.extracted_document_data import ExtractedDocumentData
from utils.logger import logger

from extract_document import fetch_document
from extract_big_part import fetch_big_parts
from extract_chapter import fetch_chapters
from extract_part import fetch_parts
from extract_mini_part import fetch_mini_parts
from extract_article import fetch_articles
from extract_article_version import fetch_article_versions
from extract_document_mapping import fetch_document_mappings
from extract_document_type import fetch_document_type
from extract_sector import fetch_sector
from extract_issuing_authority import fetch_issuing_authorities


def extract_document_data(
    connection: MySQLConnectionAbstract,
    cursor: MySQLCursorAbstract, document_id: int
) -> ExtractedDocumentData:
    start_time = time.time()

    try:
        extracted_document = fetch_document(cursor=cursor, document_id=document_id)
        extracted_big_parts = fetch_big_parts(cursor=cursor, document_id=document_id)
        extracted_chapters = fetch_chapters(cursor=cursor, document_id=document_id)
        extracted_parts = fetch_parts(cursor=cursor, document_id=document_id)
        extracted_mini_parts = fetch_mini_parts(cursor=cursor, document_id=document_id)
        extracted_articles = fetch_articles(cursor=cursor, document_id=document_id)
        extracted_article_versions = fetch_article_versions(cursor=cursor, document_id=document_id)
        extracted_document_mappings = fetch_document_mappings(cursor=cursor, document_id=document_id)
        extracted_document_type = None
        extracted_sector = None
        extracted_issuing_authorities = []

        document_type_id = extracted_document.id_loai_van_ban

        if isinstance(document_type_id, int):
            extracted_document_type = fetch_document_type(cursor=cursor, document_type_id=document_type_id)
        
        sector_id = extracted_document.id_linh_vuc

        if isinstance(sector_id, int):
            extracted_sector = fetch_sector(cursor=cursor, sector_id=sector_id)

        issuing_authority_ids = []

        try:
            issuing_authority_ids = json.loads(extracted_document.id_co_quan_ban_hanh)
        except Exception:
            pass

        if isinstance(issuing_authority_ids, list):
            extracted_issuing_authorities = fetch_issuing_authorities(
                cursor=cursor,
                issuing_authority_ids=issuing_authority_ids
            )
        
        return ExtractedDocumentData(
            extracted_document=extracted_document,
            extracted_big_parts=extracted_big_parts,
            extracted_chapters=extracted_chapters,
            extracted_parts=extracted_parts,
            extracted_mini_parts=extracted_mini_parts,
            extracted_articles=extracted_articles,
            extracted_article_versions=extracted_article_versions,
            extracted_document_mappings=extracted_document_mappings,
            extracted_document_type=extracted_document_type,
            extracted_sector=extracted_sector,
            extracted_issuing_authorities=extracted_issuing_authorities
        )
    except Exception:
        raise
    finally:
        logger.info(msg=f"{time.time() - start_time} s")
        cursor.close()
        connection.close()
    