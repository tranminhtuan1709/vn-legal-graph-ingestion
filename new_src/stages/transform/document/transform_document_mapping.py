import time
from typing import Any

from dtos.document.document_mapping_dto import DocumentMappingDto
from utils.logger import logger
from utils.datetime_utils import format_date


def transform_document_mapping_dtos(raw_document_mapping_dtos: list[dict[str, Any]]) -> list[DocumentMappingDto]:
    start_time = time.time()

    try:
        return [DocumentMappingDto(**dto) for dto in raw_document_mapping_dtos]
    except Exception:
        pass
    finally:
        logger.info(f"{time.time() - start_time} s")
    