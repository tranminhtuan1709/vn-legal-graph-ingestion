class DocumentDto:
    def __init__(
        self,
        id: int,
        so_ky_hieu: str | None,
        ten_hien_thi: str | None,
        ngay_ban_hanh: str | None,
        ngay_co_hieu_luc: str | None,
        ngay_het_han: str | None,
        trang_thai: str | None,
        chu_thich_nho: str | None,
        loai_van_ban: str | None,
        id_loai_van_ban: int | None,
        linh_vuc: str | None,
        id_linh_vuc: int | None,
        co_quan_ban_hanh: list[str],
        id_co_quan_ban_hanh: list[int]
    ) -> None:
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
