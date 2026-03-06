class ChapterDto:
    def __init__(
        self,
        id: int,
        vbpl_id: int,
        vbpl_big_part_id: int | None,
        chapter_number: str | None,
        chapter_name: str | None
    ) -> None:
        self.id = id
        self.vbpl_id = vbpl_id
        self.vbpl_big_part_id = vbpl_big_part_id
        self.chapter_number = chapter_number
        self.chapter_name = chapter_name
