from src.interface.dtos.internal.graph.base_node import BaseNode


class DocumentTypeNode(BaseNode):
    def __init__(
        self,
        document_type_id: int,
        document_type_name: str
    ) -> None:
        self.document_type_id = document_type_id
        self.document_type_name = document_type_name
