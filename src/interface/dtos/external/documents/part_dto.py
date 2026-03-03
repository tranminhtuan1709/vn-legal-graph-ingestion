class PartDto:
    def __init__(self, id: int, vbpl_id: int, vbpl_chapter_id: int, part_number: str, part_name: str) -> None:
        self.id = id
        self.vbpl_id = vbpl_id
        self.vbpl_chapter_id = vbpl_chapter_id
        self.part_number = part_number
        self.part_name = part_name
