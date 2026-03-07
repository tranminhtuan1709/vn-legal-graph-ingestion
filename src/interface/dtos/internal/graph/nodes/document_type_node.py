from interface.dtos.internal.graph.node import Node


class DocumentTypeNode(Node):    
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        source: str,
        document_type_id: int,
        document_type_name: str
    ) -> None:
        super().__init__(
            node_id=node_id,
            node_label=node_label,
            created_at=created_at,
            source=source
        )
        self.document_type_id = document_type_id
        self.document_type_name = document_type_name
