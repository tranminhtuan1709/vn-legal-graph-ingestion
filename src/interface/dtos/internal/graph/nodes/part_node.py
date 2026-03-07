from interface.dtos.internal.graph.node import Node


class PartNode(Node):
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        source: str,
        chapter_id: int,
        part_number: str,
        part_name: str
    ) -> None:
        super().__init__(
            node_id=node_id,
            node_label=node_label,
            created_at=created_at,
            source=source
        )
        
        self.chapter_id = chapter_id
        self.part_number = part_number
        self.part_name = part_name
