class ArticleVersionDto:
    def __init__(
        self,
        version_id: int,
        vbplsd_id: int,
        vbpldsd_id: int,
        dieu_sd: str,
        dieu_dsd: str,
        dieu_sd_id: int,
        dieu_dsd_id: int,
        phu_luc_sd: str | None,
        phu_luc_dsd: str | None,
        loai_vb: str,
        from_date: str | None,
        to_date: str | None,
        bai_bo_noi_dung_truoc: bool | None,
        noi_dung_sua_doi: str | None
    ) -> None:
        self.version_id = version_id
        self.vbplsd_id = vbplsd_id
        self.vbpldsd_id = vbpldsd_id
        self.dieu_sd = dieu_sd
        self.dieu_dsd = dieu_dsd
        self.dieu_sd_id = dieu_sd_id
        self.dieu_dsd_id = dieu_dsd_id
        self.phu_luc_sd = phu_luc_sd
        self.phu_luc_dsd = phu_luc_dsd
        self.loai_vb = loai_vb
        self.from_date = from_date
        self.to_date = to_date
        self.bai_bo_noi_dung_truoc = bai_bo_noi_dung_truoc
        self.noi_dung_sua_doi = noi_dung_sua_doi
