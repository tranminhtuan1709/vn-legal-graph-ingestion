from pydantic import BaseModel


class ArticleVersionDto(BaseModel):
    version_id: int
    vbplsd_id: int
    vbpldsd_id: int
    dieu_sd_id: int
    dieu_dsd_id: int
    phu_luc_sd: str | None
    phu_luc_dsd: str | None
    from_date: str | None
    to_date: str | None
    bai_bo_noi_dung_truoc: bool | None
    noi_dung_sua_doi: str | None
