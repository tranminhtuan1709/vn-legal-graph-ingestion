from dtos.graph.edges.edge import Edge
from datetime import date


class SuspendEdge(Edge):
    version_id: int
    from_date: date | None
    to_date: date | None
    