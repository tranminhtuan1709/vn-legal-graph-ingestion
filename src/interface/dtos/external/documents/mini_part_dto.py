class MiniPartDto:
    def __init__(
        self,
        id: int,
        vbpl_id: int,
        vbpl_part_id: int | None,
        mini_part_number: str | None,
        mini_part_name: str | None
    ) -> None:
        """
        Init MiniPartDto with provided attributes.

        Args:
            id (int): ID of the mini part.
            vbpl_id (int): ID of the document which contains the mini part.
            vbpl_part_id (int | None): ID of the part which contains the mini part.
            mini_part_number (str | None): Number of the mini part.
            mini_part_name (str | None): Name of the mini part.
        """
        
        self.id = id
        self.vbpl_id = vbpl_id
        self.vbpl_part_id = vbpl_part_id
        self.mini_part_number = mini_part_number
        self.mini_part_name = mini_part_name
