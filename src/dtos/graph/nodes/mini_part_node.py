from dtos.graph.nodes.node import Node


class MiniPartNode(Node):
    mini_part_id: int
    mini_part_number: str | None
    mini_part_name: str | None
    