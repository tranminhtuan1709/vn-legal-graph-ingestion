class ApprovedDocumentIdDto:
    def __init__(self, message_id: str, document_id: int, event_type: str, approved_at: str, source: str) -> None:
        """
        Init ApprovedDocumentDto with provided attributes.

        Args:
            message_id (str): ID of the message coming to Kafka.
            document_id (int): ID of the approved document.
            event_type (str): Type of event.
            approved_at (str): Timestamp when the document is approved.
            source (str): Name of the producer who sent the message to Kafka.
        """

        self.message_id = message_id
        self.document_id = document_id
        self.event_type = event_type
        self.approved_at = approved_at
        self.source = source
