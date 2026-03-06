from src.interface.dtos.internal.graph.base_node import BaseNode


class DocumentNode(BaseNode):
    def __init__(
        self,
        document_id: int,
        document_number: str,
        document_name: str,
        issued_date: str,
        effective_date: str,
        expiry_date: str,
        status: str,
        summary: str
    ) -> None:
        self.document_id = document_id
        self.document_number = document_number
        self.document_name = document_name
        self.issued_date = issued_date
        self.effective_date = effective_date
        self.expiry_date = expiry_date
        self.status = status
        self.summary = summary
