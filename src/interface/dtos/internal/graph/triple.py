from src.interface.dtos.internal.graph.edge import Edge


class Triple:
    def __init__(self, from_node_id: str, to_node_id: int, edge: Edge) -> None:
        self.from_node_id = from_node_id
        self.to_node_id = to_node_id
        self.edge = edge
