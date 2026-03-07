from interface.dtos.internal.graph.node import Node


class ArticleNode(Node):
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        source: str,
        article_id: int,
        article_number: str,
        article_name: str,
        article_content: str,
        effective_date: str,
        appendix: str
    ) -> None:
        super().__init__(
            node_id=node_id,
            node_label=node_label,
            created_at=created_at,
            source=source
        )

        self.article_id = article_id
        self.article_number = article_number
        self.article_name = article_name
        self.article_content = article_content
        self.effective_date = effective_date
        self.appendix = appendix
