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
        """
        Init ArticleDto with provided attributes.

        Args:
            id (int): ID of the article.
            vbpl_id (int): ID of the document to which the article belongs to.
            vbpl_big_part_id (int): ID of the big part to which the article belongs to.
            vbpl_chapter_id (int): ID of the chapter to which the article belongs to.
            vbpl_part_id (int): ID of the part to which the article belongs to.
            vbpl_mini_part_id (int): ID of the mini part to which the article belongs to.
            section_number (str): Number of the article.
            section_name (str): Name of the article.
            section_content (str): Content of the article (including clauses).
            so_phu_luc (str): Number of the appendix to which the article belongs to.
            effective_date (str): Effective date of the article. Date format: `yyyy-mm-dd`.
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
