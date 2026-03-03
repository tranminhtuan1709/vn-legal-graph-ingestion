class SuspendEdge:
    def __init__(self, created_at: str, from_date: str, to_date: str) -> None:
        """
        Init SuspendEdge with provided attributes.

        Args:
            created_at (str): Timestamp when this edge is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            from_date (str): Start date of the article version. Date format: `yyyy-mm-dd`.
            to_date (str): End date of the article version. Date format: `yyyy-mm-dd`.
        """

        self.created_at = created_at
        self.from_date = from_date
        self.to_date = to_date
