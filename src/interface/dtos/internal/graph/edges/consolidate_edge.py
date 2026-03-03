class ConsolidateEdge:
    def __init__(self, created_at: str, document_mapping_id: int) -> None:
        """
        Init ConsolidateEdge with provided attributes.

        Args:
            created_at (str): Timestamp when this edge is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            document_mapping_id (int): ID of the document mapping.
        """
        
        self.created_at = created_at
        self.document_mapping_id = document_mapping_id
