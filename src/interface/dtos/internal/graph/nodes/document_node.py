class DocumentNode:
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        updated_at: str,
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
        self.node_id = node_id
        self.node_label = node_label
        self.created_at = created_at
        self.updated_at = updated_at
        self.source = source
        self.document_id = document_id
        self.document_number = document_number
        self.document_name = document_name
        self.issued_date = issued_date
        self.effective_date = effective_date
        self.expiry_date = expiry_date
        self.status = status
        self.summary = summary
