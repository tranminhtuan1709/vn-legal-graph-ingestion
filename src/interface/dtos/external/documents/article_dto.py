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
        """
        Init ArticleDto with provided attributes.

        Args:
            id (int): ID of the article.
            vbpl_id (int): ID of the document to which the article belongs to.
            vbpl_big_part_id (int | None): ID of the big part to which the article belongs to.
            vbpl_chapter_id (int | None): ID of the chapter to which the article belongs to.
            vbpl_part_id (int): ID of the part to which the article belongs to.
            vbpl_mini_part_id (int | None): ID of the mini part to which the article belongs to.
            section_number (str | None): Number of the article.
            section_name (str | None): Name of the article.
            section_content (str | None): Content of the article (including clauses).
            so_phu_luc (str | None): Number of the appendix to which the article belongs to.
            effective_date (str | None): Effective date of the article. Date format: `yyyy-mm-dd`.
        """
        
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
