class PartNode:
    def __init__(self, node_id: str, created_at: str, chapter_id: int, part_number: str, part_name: str) -> None:
        """
        Init PartNode with provided attributes.

        Args:
            node_id (str): ID of the node.
            created_at (str): Timestamp when the node is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            chapter_id (int): ID of the part.
            part_number (str): Number of the part.
            part_name (str): Name of the part.
        """
        
        self.node_id = node_id
        self.created_at = created_at
        self.chapter_id = chapter_id
        self.part_number = part_number
        self.part_name = part_name
