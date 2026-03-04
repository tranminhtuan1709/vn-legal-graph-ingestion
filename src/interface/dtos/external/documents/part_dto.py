class PartDto:
    def __init__(
        self,
        id: int,
        vbpl_id: int,
        vbpl_chapter_id: int | None,
        part_number: str | None,
        part_name: str | None
    ) -> None:
        """
        Init PartDto with provided attributes.

        Args:
            id (int): ID of the part.
            vbpl_id (int): ID of the document which contains the part.
            vbpl_chapter_id (int | None): ID of the chapter which contains the part.
            part_number (str | None): Number of the part.
            part_name (str | None): Name of the part.
        """
        
        self.id = id
        self.vbpl_id = vbpl_id
        self.vbpl_chapter_id = vbpl_chapter_id
        self.part_number = part_number
        self.part_name = part_name
