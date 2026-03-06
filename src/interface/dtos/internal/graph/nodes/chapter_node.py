from src.interface.dtos.internal.graph.base_node import BaseNode


class ChapterNode(BaseNode):
    def __init__(
        self,
        chapter_id: int,
        chapter_number: str,
        chapter_name: str
    ) -> None:
        self.chapter_id = chapter_id
        self.chapter_number = chapter_number
        self.chapter_name = chapter_name
