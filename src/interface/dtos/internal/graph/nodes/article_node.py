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
        """
        Init ArticleNode with provided attributes.

        Args:
            node_id (str): ID of the node.
            created_at (str): Timestamp when the node is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            article_id (int): ID of the article.
            article_number (str): Number of the article.
            article_name (str): Name of the article.
            article_content (str): Content of the article.
            effective_date (str): Effective date of the article.
            appendix (str): Number of the appendix which contains the article.
        """

        self.node_id = node_id
        self.created_at = created_at
        self.article_id = article_id
        self.article_number = article_number
        self.article_name = article_name
        self.article_content = article_content
        self.effective_date = effective_date
        self.appendix = appendix
