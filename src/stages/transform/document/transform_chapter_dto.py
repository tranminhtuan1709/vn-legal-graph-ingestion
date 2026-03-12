from typing import Any

from dtos.document.chapter_dto import ChapterDto


def transform_chapter_dtos(raw_chapter_dtos: list[dict[str, Any]]) -> list[ChapterDto]:
    try:
        chapter_dtos = [ChapterDto(**dto) for dto in raw_chapter_dtos]

        for dto in chapter_dtos:
            for field in ["chapter_number", "chapter_name"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())

        return chapter_dtos
    except Exception:
        raise
