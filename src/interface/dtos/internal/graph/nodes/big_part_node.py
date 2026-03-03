class BigPartNode:
    def __init__(
        self,
        node_id: str,
        created_at: str,
        big_part_id: int,
        big_part_number: str,
        big_part_name: str
    ) -> None:
        """
        Init BigPartNode with provided attributes.

        Args:
            node_id (str): ID of the node.
            created_at (str): Timestamp when the node is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            big_part_id (int): ID of the big part.
            big_part_number (str): Number of the big part.
            big_part_name (str): Name of the big part.
        """
        
        self.node_id = node_id
        self.created_at = created_at
        self.big_part_id = big_part_id
        self.big_part_number = big_part_number
        self.big_part_name = big_part_name
