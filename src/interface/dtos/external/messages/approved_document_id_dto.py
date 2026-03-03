class ApprovedDocumentIdDto:
    def __init__(self, message_id: str, document_id: int, event_type: str, approved_at: str, source: str) -> None:
        self.message_id = message_id
        self.document_id = document_id
        self.event_type = event_type
        self.approved_at = approved_at
        self.source = source
