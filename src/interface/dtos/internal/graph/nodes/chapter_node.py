class ChapterNode:
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        chapter_id: int,
        chapter_number: str,
        chapter_name: str
    ) -> None:
        self.node_id = node_id
        self.node_label = node_label
        self.created_at = created_at
        self.chapter_id = chapter_id
        self.chapter_number = chapter_number
        self.chapter_name = chapter_name
