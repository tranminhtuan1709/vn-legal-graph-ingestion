from pydantic import BaseModel


class ArticleNode(BaseModel):
    node_id: str
    node_label: str
    created_at: str
    source: str
    article_id: int
    article_number: str
    article_name: str | None
    article_content: str | None
    effective_date: str | None
    appendix: str | None
    