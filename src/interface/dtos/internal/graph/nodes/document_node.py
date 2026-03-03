class DocumentNode:
    def __init__(
        self,
        node_id: str,
        created_at: str,
        document_id: int,
        document_number: str,
        document_name: str,
        issued_date: str,
        effective_date: str,
        expiry_date: str,
        status: str,
        summary: str
    ) -> None:
        """
        Init DocumentNode with provided attributes.

        Args:
            node_id (str): ID of the node.
            created_at (str): Timestamp when the node is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            document_id (int): ID of the document.
            document_number (str): Number of the document.
            document_name (str): Name of the document.
            issued_date (str): Issued date of the document.
            effective_date (str): Effective date of the document.
            expiry_date (str): Expiry date of the document.
            status (str): Status of the document.
            summary (str): Small note (subject line) of the document.
        """
        
        self.node_id = node_id
        self.created_at = created_at
        self.document_id = document_id
        self.document_number = document_number
        self.document_name = document_name
        self.issued_date = issued_date
        self.effective_date = effective_date
        self.expiry_date = expiry_date
        self.status = status
        self.summary = summary
