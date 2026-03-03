class ChapterDto:
    def __init__(self, id: int, vbpl_id: int, vbpl_big_part_id: int, chapter_number: str, chapter_name: str) -> None:
        """
        Init ChapterDto with provided attributes.

        Args:
            id (int): ID of the chapter.
            vbpl_id (int): ID of the document which contains the chapter.
            vbpl_big_part_id (int): ID of the big part which contains the chapter.
            chapter_number (str): Number of the chapter.
            chapter_name (str): Name of the chapter.
        """
        
        self.id = id
        self.vbpl_id = vbpl_id
        self.vbpl_big_part_id = vbpl_big_part_id
        self.chapter_number = chapter_number
        self.chapter_name = chapter_name
