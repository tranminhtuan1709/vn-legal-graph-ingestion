from pydantic import BaseModel
from typing import Literal


class ValidatedArticleVersion(BaseModel):
    version_id: int
    vbplsd_id: int
    vbpldsd_id: int
    dieu_sd: str | None
    dieu_dsd: str | None
    dieu_sd_id: int
    dieu_dsd_id: int
    phu_luc_sd: str | None
    phu_luc_dsd: str | None
    loai_vb: Literal["SĐ", "BS", "NHL"]
    from_date: str | None
    to_date: str | None
    bai_bo_noi_dung_truoc: int | None
    noi_dung_sua_doi: str | None
    