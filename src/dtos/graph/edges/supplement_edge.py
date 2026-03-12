from dtos.graph.edges.edge import Edge
from datetime import date


class SupplementEdge(Edge):
    version_id: int
    from_date: date | None
    to_date: date | None
    