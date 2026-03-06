class BigPartNode:
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        updated_at: str,
        source: str,
        big_part_id: int,
        big_part_number: str,
        big_part_name: str
    ) -> None:
        self.node_id = node_id
        self.node_label = node_label
        self.created_at = created_at
        self.updated_at = updated_at
        self.source = source
        self.big_part_id = big_part_id
        self.big_part_number = big_part_number
        self.big_part_name = big_part_name
