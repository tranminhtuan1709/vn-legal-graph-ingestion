import time
from typing import Any

from dtos.document.big_part_dto import BigPartDto
from utils.logger import logger


def transform_big_part_dtos(raw_big_part_dtos: list[dict[str, Any]]) -> list[BigPartDto]:
    start_time = time.time()

    try:
        big_part_dtos = [BigPartDto(**dto) for dto in raw_big_part_dtos]

        for dto in big_part_dtos:
            for field in ["big_part_numner", "big_part_name"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())

        return big_part_dtos
    except Exception:
        raise
    finally:
        logger.info(f"{time.time() - start_time} s")
    