from src.interface.dtos.internal.graph.edge import Edge


class SupplementEdge(Edge):    
    def __init__(
        self,
        edge_type: str,
        created_at: str,
        version_id: int,
        from_date: str,
        to_date: str
    ) -> None:
        super().__init__(
            edge_type=edge_type,
            created_at=created_at
        )
        
        self.version_id = version_id
        self.from_date = from_date
        self.to_date = to_date
