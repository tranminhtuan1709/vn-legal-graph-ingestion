from pydantic import BaseModel
from typing import Literal
from datetime import date


class ArticleVersionDto(BaseModel):
    version_id: int

    from_article_id: int
    from_article_number: str | None
    from_article_name: str | None
    from_article_content: str | None
    from_appendix_number: str | None
    from_effective_date: date | None

    to_article_id: int
    to_article_number: str | None
    to_article_name: str | None
    to_article_content: str | None
    to_appendix_number: str | None
    to_effective_date: date | None

    modification_type: Literal["SĐ", "BS", "NHL"]
    modification_content: str | None
    is_abolish_previous_content: bool
    from_date: date | None
    to_date: date | None
    