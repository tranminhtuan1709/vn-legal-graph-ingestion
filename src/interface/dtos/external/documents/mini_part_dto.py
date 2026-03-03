class MiniPartDto:
    def __init__(self, id: int, vbpl_id: int, vbpl_part_id: int, mini_part_number: int, mini_part_name: int) -> None:
        self.id = id
        self.vbpl_id = vbpl_id
        self.vbpl_part_id = vbpl_part_id
        self.mini_part_number = mini_part_number
        self.mini_part_name = mini_part_name
