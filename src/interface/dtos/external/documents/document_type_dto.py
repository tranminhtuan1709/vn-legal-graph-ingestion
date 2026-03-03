class DocumentTypeDto:
    def __init__(self, id: int, loai_van_ban: str) -> None:
        """
        Init DocumentTypeDto with provided attributes.

        Args:
            id (int): ID of the document type.
            loai_van_ban (str): Name of the document type.
        """
        
        self.id = id
        self.loai_van_ban = loai_van_ban
