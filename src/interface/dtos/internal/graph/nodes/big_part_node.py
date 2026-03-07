from interface.dtos.internal.graph.node import Node


class BigPartNode(Node):
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        source: str,
        big_part_id: int,
        big_part_number: str,
        big_part_name: str
    ) -> None:
        super().__init__(
            node_id=node_id,
            node_label=node_label,
            created_at=created_at,
            source=source
        )

        self.big_part_id = big_part_id
        self.big_part_number = big_part_number
        self.big_part_name = big_part_name
