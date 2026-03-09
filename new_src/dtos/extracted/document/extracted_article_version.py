from pydantic import BaseModel
from typing import Any


class ExtractedArticleVersion(BaseModel):
    version_id: Any
    vbplsd_id: Any
    vbpldsd_id: Any
    dieu_sd: Any
    dieu_dsd: Any
    dieu_sd_id: Any
    dieu_dsd_id: Any
    phu_luc_sd: Any
    phu_luc_dsd: Any
    loai_vb: Any
    from_date: Any
    to_date: Any
    bai_bo_noi_dung_truoc: Any
    noi_dung_sua_doi: Any
    