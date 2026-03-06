class DocumentTypeNode:
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        document_type_id: int,
        document_type_name: str
    ) -> None:
        self.node_id = node_id
        self.node_label = node_label
        self.created_at = created_at
        self.document_type_id = document_type_id
        self.document_type_name = document_type_name
