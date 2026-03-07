class IssueEdge:
    edge_type = "ISSUE"
    
    def __init__(self, created_at: str) -> None:
        self.created_at = created_at
