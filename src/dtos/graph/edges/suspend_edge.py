from dtos.graph.edges.edge import Edge


class SuspendEdge(Edge):
    version_id: int
    from_date: str | None
    to_date: str | None
    