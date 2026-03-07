class ArticleDto:
    def __init__(
        self,
        id: int,
        vbpl_id: int,
        vbpl_big_part_id: int | None,
        vbpl_chapter_id: int | None,
        vbpl_part_id: int | None,
        vbpl_mini_part_id: int | None,
        section_number: str | None,
        section_name: str | None,
        section_content: str | None,
        so_phu_luc: str | None,
        effective_date: str | None
    ) -> None:
        self.id = id
        self.vbpl_id = vbpl_id
        self.vbpl_big_part_id = vbpl_big_part_id
        self.vbpl_chapter_id = vbpl_chapter_id
        self.vbpl_part_id = vbpl_part_id
        self.vbpl_mini_part_id = vbpl_mini_part_id
        self.section_number = section_number
        self.section_name = section_name
        self.section_content = section_content
        self.so_phu_luc = so_phu_luc
        self.effective_date = effective_date
