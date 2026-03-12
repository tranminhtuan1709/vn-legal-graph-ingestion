from typing import Any

from dtos.document.article_dto import ArticleDto


def transform_article_dtos(raw_article_dtos: list[dict[str, Any]]) -> list[ArticleDto]:
    try:
        article_dtos = [ArticleDto(**dto) for dto in raw_article_dtos]

        for dto in article_dtos:
            for field in ["article_number", "article_name", "article_content", "appendix_number"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())
        
        return article_dtos
    except Exception:
        raise
