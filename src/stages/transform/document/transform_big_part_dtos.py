from typing import Any

from dtos.document.big_part_dto import BigPartDto


def transform_big_part_dtos(raw_big_part_dtos: list[dict[str, Any]]) -> list[BigPartDto]:
    if len(raw_big_part_dtos) == 0:
        return []
    
    try:
        big_part_dtos = [BigPartDto(**dto) for dto in raw_big_part_dtos]

        for dto in big_part_dtos:
            for field in ["big_part_number", "big_part_name"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())

        return big_part_dtos
    except Exception:
        raise
