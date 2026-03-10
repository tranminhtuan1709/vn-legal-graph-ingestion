import time
from typing import Any

from dtos.document.part_dto import PartDto
from utils.logger import logger


def transform_part_dtos(raw_part_dtos: list[dict[str, Any]]) -> list[PartDto]:
    start_time = time.time()

    try:
        part_dtos = [PartDto(**dto) for dto in raw_part_dtos]

        for dto in part_dtos:
            for field in ["part_number", "part_name"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())

        return part_dtos
    except Exception:
        raise
    finally:
        logger.info(f"{time.time() - start_time} s")
    