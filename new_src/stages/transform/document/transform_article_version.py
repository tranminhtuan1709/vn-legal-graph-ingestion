import time
from typing import Any

from dtos.document.article_version_dto import ArticleVersionDto
from utils.logger import logger
from utils.datetime_utils import format_date


def transform_article_version_dtos(raw_article_version_dtos: list[dict[str, Any]]) -> list[ArticleVersionDto]:
    start_time = time.time()

    try:
        article_version_dtos = []

        for dto in raw_article_version_dtos:
            article_version_dtos.append(
                ArticleVersionDto(
                    version_id=dto.get("version_id"),
                    vbplsd_id=dto.get("vbplsd_id"),
                    vbpldsd_id=dto.get("vbpldsd_id"),
                    dieu_sd=dto.get("dieu_sd"),
                    dieu_dsd=dto.get("dieu_dsd"),
                    dieu_sd_id=dto.get("dieu_sd_id"),
                    dieu_dsd_id=dto.get("dieu_dsd_id"),
                    phu_luc_sd=dto.get("phu_luc_sd"),
                    phu_luc_dsd=dto.get("phu_luc_dsd"),
                    loai_vb=dto.get("loai_vb"),
                    from_date=dto.get("from_date"),
                    to_date=dto.get("to_date"),
                    bai_bo_noi_dung_truoc=bool(dto.get("bai_bo_noi_dung_truoc")),
                    noi_dung_sua_doi=dto.get("noi_dung_sua_doi"),
                )
            )

        for dto in article_version_dtos:
            for field in ["dieu_sd", "dieu_dsd", "phu_luc_sd", "phu_luc_dsd", "noi_dung_sua_doi"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, value.lower().strip())

            for field in ["from_date", "to_date"]:
                value = dto.__getattribute__(field)

                if isinstance(value, str):
                    dto.__setattr__(field, format_date(input=value, format="%Y-%m-%d"))

        return article_version_dtos
    except Exception:
        pass
    finally:
        logger.info(f"{time.time() - start_time} s")
