class MiniPartNode:
    def __init__(
        self,
        node_id: str,
        created_at: str,
        chapter_id: int,
        mini_part_number: str,
        mini_part_name: str
    ) -> None:
        """
        Init MiniPartNode with provided attributes.

        Args:
            node_id (str): ID of the node.
            created_at (str): Timestamp when the node is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            chapter_id (int): ID fo the chapter.
            mini_part_number (str): Number of the chapter.
            mini_part_name (str): Name of the chapter.
        """
        
        self.node_id = node_id
        self.created_at = created_at
        self.chapter_id = chapter_id
        self.mini_part_number = mini_part_number
        self.mini_part_name = mini_part_name
