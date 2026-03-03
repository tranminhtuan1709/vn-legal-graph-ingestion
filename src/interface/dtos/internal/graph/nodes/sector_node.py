class SectorNode:
    def __init__(self, node_id: str, created_at: str, sector_id: int, sector_name: str) -> None:
        """
        Init SectorNode with provided attributes.

        Args:
            node_id (str): ID of the node.
            created_at (str): Timestamp when the node is crrated. Datetime format: `yyyy-mm-dd hh:mm:ss`.
            sector_id (int): ID of the sector.
            sector_name (str): Name of the sector.
        """
        
        self.node_id = node_id
        self.created_at = created_at
        self.sector_id = sector_id
        self.sector_name = sector_name
