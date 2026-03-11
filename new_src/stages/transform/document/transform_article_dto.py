import time
from typing import Any

from dtos.document.article_dto import ArticleDto
from utils.logger import logger


def transform_article_dtos(raw_article_dtos: list[dict[str, Any]]) -> list[ArticleDto]:
    start_time = time.time()

    try:
        article_dtos = [ArticleDto(**dto) for dto in raw_article_dtos]

        for dto in article_dtos:
            for field in ["article_number", "article_name", "article_content", "appendix"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())
        
        return article_dtos
    except Exception:
        pass
    finally:
        logger.info(f"{time.time() - start_time} s")
    