class IssuingAuthorityNode:
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        updated_at: str,
        source: str,
        issuing_authority_id: int,
        issuing_authority_name: str
    ) -> None:
        self.node_id = node_id
        self.node_label = node_label
        self.created_at = created_at
        self.updated_at = updated_at
        self.source = source
        self.issuing_authority_id = issuing_authority_id
        self.issuing_authority_name = issuing_authority_name
