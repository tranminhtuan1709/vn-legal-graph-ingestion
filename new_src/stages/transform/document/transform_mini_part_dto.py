import time
from typing import Any

from dtos.document.mini_part_dto import MiniPartDto
from utils.logger import logger


def transform_mini_part_dtos(raw_mini_part_dtos: list[dict[str, Any]]) -> list[MiniPartDto]:
    start_time = time.time()

    try:
        mini_part_dtos = [MiniPartDto(**dto) for dto in raw_mini_part_dtos]

        for dto in mini_part_dtos:
            for field in ["mini_part_numner", "mini_part_name"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())

        return mini_part_dtos
    except Exception:
        raise
    finally:
        logger.info(f"{time.time() - start_time} s")
    