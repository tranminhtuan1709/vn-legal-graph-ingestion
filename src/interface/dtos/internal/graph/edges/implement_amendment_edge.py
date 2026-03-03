class ImplementAmendmentEdge:
    def __init__(
        self,
        created_at: str,
        version_id: int,
        from_date: str,
        to_date: str,
        abolish_previous_content: bool
    ) -> None:
        """
        Init ImplementAmendmentEdge with provided attributes.

        Args:
            created_at (str): Timestamp when this edge is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            version_id (int): ID of the article version.
            from_date (str): Start date of the article version. Date format: `yyyy-mm-dd`.
            to_date (str): End date of the article version. Date format: `yyyy-mm-dd`.
            abolish_previous_content (bool): Whether this version abolish the previous content.
        """

        self.created_at = created_at
        self.version_id = version_id
        self.from_date = from_date
        self.to_date = to_date
        self.abolish_previous_content = abolish_previous_content
