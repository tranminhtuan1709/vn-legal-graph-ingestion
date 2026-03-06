from src.interface.dtos.internal.graph.base_edge import BaseEdge


class SupplementEdge(BaseEdge):
    def __init__(self, version_id: int, from_date: str, to_date: str) -> None:
        self.version_id = version_id
        self.from_date = from_date
        self.to_date = to_date
