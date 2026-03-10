from dtos.graph.edges.edge import Edge


class SupplementEdge(Edge):
    from_date: str | None
    to_date: str | None
    