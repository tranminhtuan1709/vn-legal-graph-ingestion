class SuspendEdge:
    edge_type = "SUSPEND"
    
    def __init__(self, created_at: str, from_date: str, to_date: str) -> None:
        self.created_at = created_at
        self.from_date = from_date
        self.to_date = to_date
