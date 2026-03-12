from typing import Any

from dtos.document.document_mapping_dto import DocumentMappingDto


def transform_document_mapping_dtos(raw_document_mapping_dtos: list[dict[str, Any]]) -> list[DocumentMappingDto]:
    try:
        document_mapping_dtos = [DocumentMappingDto(**dto) for dto in raw_document_mapping_dtos]

        for dto in document_mapping_dtos:
            for field in ["from_document_number", "to_document_number"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.upper().strip())

            for field in [
                "from_document_name", "from_status", "from_small_note",
                "to_document_name", "to_status", "to_small_note"
            ]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())
        
        return document_mapping_dtos
    except Exception:
        raise
