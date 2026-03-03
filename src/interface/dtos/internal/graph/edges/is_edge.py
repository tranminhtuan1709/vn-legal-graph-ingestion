class IsEdge:
    def __init__(self, created_at: str) -> None:
        """
        Init IsEdge with provided attributes.

        Args:
            created_at (str): Timestamp when this edge is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
        """
        
        self.created_at = created_at
