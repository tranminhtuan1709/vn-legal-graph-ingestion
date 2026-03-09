from pydantic import BaseModel
from typing import Any


class ExtractedDocument(BaseModel):
    id: Any
    so_ky_hieu: Any
    ten_hien_thi: Any
    ngay_ban_hanh: Any
    ngay_co_hieu_luc: Any
    ngay_het_han: Any
    trang_thai: Any
    chu_thich_nho: Any
    loai_van_ban: Any
    linh_vuc: Any
    co_quan_ban_hanh: Any
    id_loai_van_ban: Any
    id_linh_vuc: Any
    id_co_quan_ban_hanh: Any
    