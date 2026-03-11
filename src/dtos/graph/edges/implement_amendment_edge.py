from dtos.graph.edges.edge import Edge


class ImplementAmendmentEdge(Edge):
    version_id: int
    from_date: str | None
    to_date: str | None
    is_abolish_previous_content: bool
    