from dtos.graph.edges.edge import Edge


class SupplementEdge(Edge):
    version_id: int
    from_date: str | None
    to_date: str | None
    