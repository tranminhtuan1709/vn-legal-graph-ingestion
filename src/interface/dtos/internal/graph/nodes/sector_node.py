from src.interface.dtos.internal.graph.base_node import BaseNode


class SectorNode(BaseNode):
    def __init__(
        self,
        sector_id: int,
        sector_name: str
    ) -> None:
        self.sector_id = sector_id
        self.sector_name = sector_name
