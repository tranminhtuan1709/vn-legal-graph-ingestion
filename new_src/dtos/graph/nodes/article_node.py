from dtos.graph.nodes.node import Node


class ArticleNode(Node):
    article_id: int
    article_number: str | None
    article_name: str | None
    article_content: str | None
    effective_date: str | None
    appendix: str | None
    