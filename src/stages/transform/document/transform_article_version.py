import time
from typing import Any

from dtos.document.article_version_dto import ArticleVersionDto
from utils.logger import logger


def transform_article_version_dtos(raw_article_version_dtos: list[dict[str, Any]]) -> list[ArticleVersionDto]:
    start_time = time.time()

    try:
        article_version_dtos: list[ArticleVersionDto] = []

        for dto in raw_article_version_dtos:
            article_version_dtos.append(
                ArticleVersionDto(
                    version_id=dto.get("version_id"),

                    from_article_id=dto.get("from_article_id"),
                    from_article_number=dto.get("from_article_number"),
                    from_article_name=dto.get("from_article_name"),
                    from_article_content=dto.get("from_article_content"),
                    from_appendix_number=dto.get("from_appendix_number"),
                    from_effective_date=dto.get("from_effective_date"),

                    to_article_id=dto.get("to_article_id"),
                    to_article_number=dto.get("to_article_number"),
                    to_article_name=dto.get("to_article_name"),
                    to_article_content=dto.get("to_article_content"),
                    to_appendix_number=dto.get("to_appendix_number"),
                    to_effective_date=dto.get("to_effective_date"),

                    modification_type=dto.get("modification_type"),
                    modification_content=dto.get("modification_content"),
                    is_abolish_previous_content=dto.get("is_abolish_previous_content"),
                    from_date=dto.get("from_date"),
                    to_date=dto.get("to_date")
                )
            )

        for dto in article_version_dtos:
            for field in [
                "from_article_number", "from_article_name", "from_article_content", "from_appendix_number",
                "to_article_number", "to_article_name", "to_article_content", "to_appendix_number",
                "modification_content"
            ]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())

        return article_version_dtos
    except Exception:
        pass
    finally:
        logger.info(f"{time.time() - start_time} s")
    