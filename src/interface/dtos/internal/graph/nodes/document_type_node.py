class DocumentTypeNode:
    def __init__(self, node_id: str, created_at: str, document_type_id: int, document_type_name: str) -> None:
        """
        Init DocumentTypeNode with provided attributes.

        Args:
            node_id (str): ID of the node.
            created_at (str): Timestamp when the node is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            document_type_id (int): ID of the document type.
            document_type_name (str): Name of the document type.
        """
        
        self.node_id = node_id
        self.created_at = created_at
        self.document_type_id = document_type_id
        self.document_type_name = document_type_name
