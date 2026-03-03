class SupplementEdge:
    def __init__(self, created_at: str, version_id: int, from_date: str, to_date: str) -> None:
        """
        Init SupplementEdge with provided attributes.

        Args:
            created_at (str): Timestamp when this edge is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            version_id (int): ID of the version.
            from_date (str): Start date of the version. Date format: `yyyy-mm-dd`.
            to_date (str): End date of the version. Date format: `yyyy-mm-dd`.
        """

        self.created_at = created_at
        self.version_id = version_id
        self.from_date = from_date
        self.to_date = to_date
