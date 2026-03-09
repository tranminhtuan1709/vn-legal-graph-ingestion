from pydantic import BaseModel


class NormalizedDocument(BaseModel):
    id: int
    so_ky_hieu: str | None
    ten_hien_thi: str | None
    ngay_ban_hanh: str | None
    ngay_co_hieu_luc: str | None
    ngay_het_han: str | None
    trang_thai: str | None
    chu_thich_nho: str | None
    loai_van_ban: str | None
    linh_vuc: str | None
    co_quan_ban_hanh: list[str | None]
    id_loai_van_ban: int | None
    id_linh_vuc: int | None
    id_co_quan_ban_hanh: list[int | None]
    