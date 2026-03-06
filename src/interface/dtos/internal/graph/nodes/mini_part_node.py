class MiniPartNode:
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        chapter_id: int,
        mini_part_number: str,
        mini_part_name: str
    ) -> None:
        self.node_id = node_id
        self.node_label = node_label
        self.created_at = created_at
        self.chapter_id = chapter_id
        self.mini_part_number = mini_part_number
        self.mini_part_name = mini_part_name
