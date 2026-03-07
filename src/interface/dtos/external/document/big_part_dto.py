class BigPartDto:
    def __init__(
        self,
        id: int,
        vbpl_id: int,
        big_part_number: str | None,
        big_part_name: str | None
    ) -> None:
        self.id = id
        self.vbpl_id = vbpl_id
        self.big_part_number = big_part_number
        self.big_part_name = big_part_name
