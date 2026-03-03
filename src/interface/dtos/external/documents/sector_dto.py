class SectorDto:
    def __init__(self, id: int, linh_vuc: str) -> None:
        """
        Init SectorDto with provided attributes.

        Args:
            id (int): ID of the sector.
            linh_vuc (str): Name of the sector.
        """
        
        self.id = id
        self.linh_vuc = linh_vuc
