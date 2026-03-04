class DocumentMappingDto:
    def __init__(
        self,
        id: int,
        from_document_id: int,
        to_document_id: int,
        relationship_type: str
    ) -> None:
        """
        Init DocumentMappingDto with provided attributes.

        Args:
            id (int): ID of the document mapping.
            from_document_id (int): ID of the modifying document.
            to_document_id (int): ID of the modified document.
            relationship_type (str): Relationship between 2 documents.
        """
        
        self.id = id
        self.from_document_id = from_document_id
        self.to_document_id = to_document_id
        self.relationship_type = relationship_type
