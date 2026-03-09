from interface.dtos.internal.graph.edge import Edge


class ReplaceEdge(Edge):
    def __init__(self, edge_type: str, created_at: str, document_mapping_id: int) -> None:
        super().__init__(
            edge_type=edge_type,
            created_at=created_at
        )
        
        self.document_mapping_id = document_mapping_id
