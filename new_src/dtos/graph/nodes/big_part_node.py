from dtos.graph.nodes.node import Node


class BigPartNode(Node):
    big_part_id: int
    big_part_number: str | None
    big_part_name: str | None
    