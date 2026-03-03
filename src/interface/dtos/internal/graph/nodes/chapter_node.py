class ChapterNode:
    def __init__(self, node_id: str, created_at: str, chapter_id: int, chapter_number: str, chapter_name: str) -> None:
        """
        Init ChapterNode with provided attributes.

        Args:
            node_id (str): ID of the node.
            created_at (str): Timestamp when the node is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            chapter_id (int): ID of the chapter.
            chapter_number (str): Number of the chapter.
            chapter_name (str): Name of the chapter.
        """
        
        self.node_id = node_id
        self.created_at = created_at
        self.chapter_id = chapter_id
        self.chapter_number = chapter_number
        self.chapter_name = chapter_name
