from src.interface.dtos.internal.graph.base_node import BaseNode


class PartNode(BaseNode):
    def __init__(
        self,
        chapter_id: int,
        part_number: str,
        part_name: str
    ) -> None:
        self.chapter_id = chapter_id
        self.part_number = part_number
        self.part_name = part_name
