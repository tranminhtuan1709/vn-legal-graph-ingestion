class IssuingAuthorityNode:
    def __init__(self, node_id: str, created_at: str, issuing_authority_id: int, issuing_authority_name: str) -> None:
        """
        Init IssuingAuthorityNode with provided attributes.

        Args:
            node_id (str): ID of the node.
            created_at (str): Timestamp when the node is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            issuing_authority_id (int): ID of the issuing authority.
            issuing_authority_name (str): Name of the issuing authority.
        """
        
        self.node_id = node_id
        self.created_at = created_at
        self.issuing_authority_id = issuing_authority_id
        self.issuing_authority_name = issuing_authority_name
