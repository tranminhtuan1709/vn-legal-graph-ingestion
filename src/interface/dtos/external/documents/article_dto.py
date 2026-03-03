class ArticleDto:
    def __init__(
        self,
        id: int,
        vbpl_id: int,
        vbpl_big_part_id: int,
        vbpl_chapter_id: int,
        vbpl_part_id: int,
        vbpl_mini_part_id: int,
        section_number: str,
        section_name: str,
        section_content: str,
        so_phu_luc: str,
        effective_date: str
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
