from dtos.graph.nodes.node import Node
from datetime import date


class ArticleNode(Node):
    article_id: int
    article_number: str | None
    article_name: str | None
    article_content: str | None
    appendix_number: str | None
    effective_date: date | None
    