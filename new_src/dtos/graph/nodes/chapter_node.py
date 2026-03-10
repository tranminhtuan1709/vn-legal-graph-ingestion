from node import Node


class ChapterNode(Node):
    chapter_id: int
    chapter_number: str | None
    chapter_name: str | None
    