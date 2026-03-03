class IssuingAuthorityNode:
    def __init__(self, node_id: str, created_at: str, issuing_authority_id: int, issuing_authority_name: str) -> None:
        self.node_id = node_id
        self.created_at = created_at
        self.issuing_authority_id = issuing_authority_id
        self.issuing_authority_name = issuing_authority_name
