class BigPartDto:
    def __init__(
        self,
        id: int,
        vbpl_id: int,
        big_part_number: str | None,
        big_part_name: str | None
    ) -> None:
        """
        Init BigPartDto with provided attributes.

        Args:
            id (int): ID of the big part.
            vbpl_id (int): ID of the document which contains the big part.
            big_part_number (str | None): Number of the big part.
            big_part_name (str | None): Name of the big part.
        """

        self.id = id
        self.vbpl_id = vbpl_id
        self.big_part_number = big_part_number
        self.big_part_name = big_part_name
