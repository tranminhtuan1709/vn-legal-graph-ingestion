from src.interface.dtos.internal.graph.node import Node


class SectorNode(Node):
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        source: str,
        sector_id: int,
        sector_name: str
    ) -> None:
        super().__init__(
            node_id=node_id,
            node_label=node_label,
            created_at=created_at,
            source=source
        )
        
        self.sector_id = sector_id
        self.sector_name = sector_name
