class DocumentMappingDto:
    def __init__(
        self,
        id: int,
        from_document_id: int,
        to_document_id: int,
        relationship_type: str
    ) -> None:
        self.id = id
        self.from_document_id = from_document_id
        self.to_document_id = to_document_id
        self.relationship_type = relationship_type
