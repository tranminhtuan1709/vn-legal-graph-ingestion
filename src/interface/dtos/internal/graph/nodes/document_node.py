from interface.dtos.internal.graph.node import Node


class DocumentNode(Node):
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        source: str,
        document_id: int,
        document_number: str,
        document_name: str,
        issued_date: str,
        effective_date: str,
        expiry_date: str,
        status: str,
        summary: str
    ) -> None:
        super().__init__(
            node_id=node_id,
            node_label=node_label,
            created_at=created_at,
            source=source
        )

        self.document_id = document_id
        self.document_number = document_number
        self.document_name = document_name
        self.issued_date = issued_date
        self.effective_date = effective_date
        self.expiry_date = expiry_date
        self.status = status
        self.summary = summary
