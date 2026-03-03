class ChapterDto:
    def __init__(self, id: int, vbpl_id: int, vbpl_big_part_id: int, chapter_number: str, chapter_name: str) -> None:
        self.id = id
        self.vbpl_id = vbpl_id
        self.vbpl_big_part_id = vbpl_big_part_id
        self.chapter_number = chapter_number
        self.chapter_name = chapter_name
