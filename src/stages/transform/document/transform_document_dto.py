import time
import json
from typing import Any

from dtos.document.document_dto import DocumentDto
from utils.logger import logger


def transform_document_dto(raw_document_dto: dict[str, Any]) -> DocumentDto:
    start_time = time.time()

    try:
        issuing_authorities = raw_document_dto.get("issuing_authorities")
        issuing_authority_ids = raw_document_dto.get("issuing_authority_ids")

        list_issuing_authorities = []
        list_issuing_authority_ids = []

        if isinstance(issuing_authorities, str):
            list_issuing_authorities = issuing_authorities.split(",")

        if isinstance(issuing_authority_ids, str):
            list_issuing_authority_ids = json.loads(issuing_authority_ids)      
        
        document_dto = DocumentDto(
            document_id=raw_document_dto.get("document_id"),
            document_number=raw_document_dto.get("document_number"),
            document_name=raw_document_dto.get("document_name"),
            issued_date=raw_document_dto.get("issued_date"),
            effective_date=raw_document_dto.get("effective_date"),
            expiry_date=raw_document_dto.get("expiry_date"),
            status=raw_document_dto.get("status"),
            small_note=raw_document_dto.get("small_note"),
            document_type=raw_document_dto.get("document_type"),
            sector=raw_document_dto.get("sector"),
            issuing_authorities=list_issuing_authorities,
            document_type_id=raw_document_dto.get("document_type_id"),
            sector_id=raw_document_dto.get("sector_id"),
            issuing_authority_ids=list_issuing_authority_ids,
        )

        if isinstance(document_dto.document_number, str):
            document_dto.document_number = document_dto.document_number.upper().strip()

        for field in ["document_name", "status", "small_note", "document_type", "sector"]:
            value = document_dto.__getattribute__(field)

            if isinstance(value, str):
                document_dto.__setattr__(field, value.lower().strip())
        
        if len(document_dto.issuing_authorities) > 0:
            document_dto.issuing_authorities = [item.lower().strip() for item in document_dto.issuing_authorities]
        
        return document_dto
    except Exception:
        raise
    finally:
        logger.info(f"{time.time() - start_time} s")
    