class GuideEdge:
    edge_type = "GUIDE"
    
    def __init__(self, created_at: str, document_mapping_id: int) -> None:
        self.created_at = created_at
        self.document_mapping_id = document_mapping_id
