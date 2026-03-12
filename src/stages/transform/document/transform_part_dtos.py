from typing import Any

from dtos.document.part_dto import PartDto


def transform_part_dtos(raw_part_dtos: list[dict[str, Any]]) -> list[PartDto]:
    if len(raw_part_dtos) == 0:
        return []
    
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
