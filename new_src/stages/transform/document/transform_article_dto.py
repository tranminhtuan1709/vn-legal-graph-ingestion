import time
from typing import Any

from dtos.document.article_dto import ArticleDto
from utils.logger import logger
from utils.datetime_utils import format_date


def transform_article_dtos(raw_article_dtos: list[dict[str, Any]]) -> list[ArticleDto]:
    start_time = time.time()

    try:
        article_dtos = [ArticleDto(**dto) for dto in raw_article_dtos]

        for dto in article_dtos:
            for field in ["section_number", "section_name", "section_content", "so_phu_luc"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())
        
            if isinstance(dto.effective_date, str):
                dto.effective_date = format_date(input=dto.effective_date, format="%Y-%m-%d")
        
        return article_dtos
    except Exception:
        pass
    finally:
        logger.info(f"{time.time() - start_time} s")
    