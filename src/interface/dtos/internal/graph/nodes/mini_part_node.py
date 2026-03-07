from interface.dtos.internal.graph.node import Node


class MiniPartNode(Node):    
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        source: str,
        chapter_id: int,
        mini_part_number: str,
        mini_part_name: str
    ) -> None:
        super().__init__(
            node_id=node_id,
            node_label=node_label,
            created_at=created_at,
            source=source
        )

        self.chapter_id = chapter_id
        self.mini_part_number = mini_part_number
        self.mini_part_name = mini_part_name
