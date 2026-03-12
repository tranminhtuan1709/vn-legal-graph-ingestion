from dtos.graph.edges.edge import Edge
from datetime import date


class ImplementAmendmentEdge(Edge):
    version_id: int
    from_date: date | None
    to_date: date | None
    is_abolish_previous_content: bool
    