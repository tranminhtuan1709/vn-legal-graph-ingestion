from src.interface.dtos.internal.graph.base_node import BaseNode


class BigPartNode(BaseNode):
    def __init__(
        self,
        big_part_id: int,
        big_part_number: str,
        big_part_name: str
    ) -> None:
        self.big_part_id = big_part_id
        self.big_part_number = big_part_number
        self.big_part_name = big_part_name
