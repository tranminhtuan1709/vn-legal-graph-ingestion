from dtos.graph.nodes.node import Node


class PartNode(Node):
    part_id: int
    part_number: str | None
    part_name: str | None
    