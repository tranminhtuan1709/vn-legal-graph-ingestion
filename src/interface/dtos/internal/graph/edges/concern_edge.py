from interface.dtos.internal.graph.edge import Edge


class ConcernEdge(Edge):
    def __init__(self, edge_type: str, created_at: str) -> None:
        super().__init__(
            edge_type=edge_type,
            created_at=created_at
        )
