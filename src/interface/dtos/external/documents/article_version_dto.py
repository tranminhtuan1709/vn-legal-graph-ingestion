class ArticleVersionDto:
    def __init__(
        self,
        version_id: int,
        vbplsd_id: int,
        vbpldsd_id: int,
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
        """
        Init ArticleVersionDto with provided attributes.

        Args:
            version_id (int): ID of the version of the article.
            vbplsd_id (int): ID of the document which contains the modyfying article.
            vbpldsd_id (int): ID of the document which contains the modified article.
            dieu_sd_id (int): ID of the modifying article.
            dieu_dsd_id (int): ID of the modified article.
            phu_luc_sd (str | None): Number of the appendix which contains the modifying article.
            phu_luc_dsd (str | None): Number of the appendix which contains the modified article.
            from_date (str | None): Start date of the version. Date format: `yyyy-mm-dd`.
            to_date (str | None): End date of this version. Date format: `yyyy-mm-dd`.
            bai_bo_noi_dung_truoc (bool | None): Whether this version abolish the previous content.
            noi_dung_sua_doi (str | None): Modification content of the version.
        """

        self.version_id = version_id
        self.vbplsd_id = vbplsd_id
        self.vbpldsd_id = vbpldsd_id
        self.dieu_sd_id = dieu_sd_id
        self.dieu_dsd_id = dieu_dsd_id
        self.phu_luc_sd = phu_luc_sd
        self.phu_luc_dsd = phu_luc_dsd
        self.loai_vb = loai_vb
        self.from_date = from_date
        self.to_date = to_date
        self.bai_bo_noi_dung_truoc = bai_bo_noi_dung_truoc
        self.noi_dung_sua_doi = noi_dung_sua_doi
