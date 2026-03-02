from pydantic import BaseModel


class ArticleNode(BaseModel):
    node_id: str
    created_at: str
    article_id: int
    article_number: str | None
    article_name: str | None
    article_content: str | None
    effective_date: str | None
    appendix: str | None
