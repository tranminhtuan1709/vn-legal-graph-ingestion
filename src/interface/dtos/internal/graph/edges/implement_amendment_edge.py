class ImplementAmendmentEdge:
    def __init__(
        self,
        created_at: str,
        version_id: int,
        from_date: str,
        to_date: str,
        abolish_previous_content: bool
    ) -> None:
        self.created_at = created_at
        self.version_id = version_id
        self.from_date = from_date
        self.to_date = to_date
        self.abolish_previous_content = abolish_previous_content
