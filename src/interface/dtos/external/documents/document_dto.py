class DocumentDto:
    def __init__(
        self,
        id: int,
        so_ky_hieu: str,
        ten_hien_thi: str,
        ngay_ban_hanh: str,
        ngay_co_hieu_luc: str,
        ngay_het_han: str,
        trang_thai: str,
        chu_thich_nho: str,
        loai_van_ban: str,
        id_loai_van_ban: int,
        linh_vuc: str,
        id_linh_vuc: int,
        co_quan_ban_hanh: list[str],
        id_co_quan_ban_hanh: list[int]
    ) -> None:
        """
        Init DocumentDto with provided attributes.

        Args:
            id (int): ID of the document.
            so_ky_hieu (str): Number of the document.
            ten_hien_thi (str): Fullname of the document.
            ngay_ban_hanh (str): Issued date of the document. Date format: `yyyy-mm-dd`.
            ngay_co_hieu_luc (str): Effective date of the document. Date format: `yyyy-mm-dd`.
            ngay_het_han (str): Expiry date of the document.Date format: `yyyy-mm-dd`.
            trang_thai (str): Status of the document.
            chu_thich_nho (str): Small note (subject line) of the document.
            loai_van_ban (str): Document type.
            id_loai_van_ban (int): ID of the document type.
            linh_vuc (str): Document sector.
            id_linh_vuc (int): ID of the document sector.
            co_quan_ban_hanh (list[str]): List of issuing authorities (each one separated by a comma).
            id_co_quan_ban_hanh (list[int]): List of ID of issuing authorities.
        """
        
        self.id = id
        self.so_ky_hieu = so_ky_hieu
        self.ten_hien_thi = ten_hien_thi
        self.ngay_ban_hanh = ngay_ban_hanh
        self.ngay_co_hieu_luc = ngay_co_hieu_luc
        self.ngay_het_han = ngay_het_han
        self.trang_thai = trang_thai
        self.chu_thich_nho = chu_thich_nho
        self.loai_van_ban = loai_van_ban
        self.id_loai_van_ban = id_loai_van_ban
        self.linh_vuc = linh_vuc
        self.id_linh_vuc = id_linh_vuc
        self.co_quan_ban_hanh = co_quan_ban_hanh
        self.id_co_quan_ban_hanh = id_co_quan_ban_hanh
