class ArticleNode:
    def __init__(
        self,
        node_id: str,
        created_at: str,
        article_id: int,
        article_number: str,
        article_name: str,
        article_content: str,
        effective_date: str,
        appendix: str
    ) -> None:
        self.node_id = node_id
        self.created_at = created_at
        self.article_id = article_id
        self.article_number = article_number
        self.article_name = article_name
        self.article_content = article_content
        self.effective_date = effective_date
        self.appendix = appendix
