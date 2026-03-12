from typing import Any

from dtos.document.mini_part_dto import MiniPartDto


def transform_mini_part_dtos(raw_mini_part_dtos: list[dict[str, Any]]) -> list[MiniPartDto]:
    try:
        mini_part_dtos = [MiniPartDto(**dto) for dto in raw_mini_part_dtos]

        for dto in mini_part_dtos:
            for field in ["mini_part_number", "mini_part_name"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())

        return mini_part_dtos
    except Exception:
        raise
