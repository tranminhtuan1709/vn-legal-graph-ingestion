class IssuingAuthorityDto:
    def __init__(self, id: int, co_quan_ban_hanh: str) -> None:
        """
        Init IssuingAuthorityDto with provided attributes.

        Args:
            id (int): ID of the issuing authority.
            co_quan_ban_hanh (str): Name of the issuing authority.
        """

        self.id = id
        self.co_quan_ban_hanh = co_quan_ban_hanh
