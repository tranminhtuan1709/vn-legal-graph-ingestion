from src.interface.dtos.internal.graph.base_node import BaseNode


class MiniPartNode(BaseNode):
    def __init__(
        self,
        chapter_id: int,
        mini_part_number: str,
        mini_part_name: str
    ) -> None:
        self.chapter_id = chapter_id
        self.mini_part_number = mini_part_number
        self.mini_part_name = mini_part_name
