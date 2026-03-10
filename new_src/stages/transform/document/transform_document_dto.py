import time
import json
from typing import Any

from dtos.document.document_dto import DocumentDto
from utils.logger import logger
from utils.datetime_utils import format_date


def transform_document_dto(raw_document_dto: dict[str, Any]) -> DocumentDto:
    start_time = time.time()

    try:
        co_quan_ban_hanh = raw_document_dto.get("co_quan_ban_hanh")
        id_co_quan_ban_hanh = raw_document_dto.get("id_co_quan_ban_hanh")

        list_co_quan_ban_hanh = []
        list_id_co_quan_ban_hanh = []

        if isinstance(co_quan_ban_hanh, str):
            list_co_quan_ban_hanh = co_quan_ban_hanh.split(",")

        if isinstance(id_co_quan_ban_hanh, str):
            list_id_co_quan_ban_hanh = json.loads(id_co_quan_ban_hanh)      
        
        document_dto = DocumentDto(
            id=raw_document_dto.get("id"),
            so_ky_hieu=raw_document_dto.get("so_ky_hieu"),
            ten_hien_thi=raw_document_dto.get("ten_hien_thi"),
            ngay_ban_hanh=raw_document_dto.get("ngay_ban_hanh"),
            ngay_co_hieu_luc=raw_document_dto.get("ngay_co_hieu_luc"),
            ngay_het_han=raw_document_dto.get("ngay_het_han"),
            trang_thai=raw_document_dto.get("trang_thai"),
            chu_thich_nho=raw_document_dto.get("chu_thich_nho"),
            loai_van_ban=raw_document_dto.get("loai_van_ban"),
            linh_vuc=raw_document_dto.get("linh_vuc"),
            co_quan_ban_hanh=list_co_quan_ban_hanh,
            id_loai_van_ban=raw_document_dto.get("id_loai_van_ban"),
            id_linh_vuc=raw_document_dto.get("id_linh_vuc"),
            id_co_quan_ban_hanh=list_id_co_quan_ban_hanh,
        )

        for field in ["so_ky_hieu", "ten_hien_thi", "trang_thai", "chu_thich_nho", "loai_van_ban", "linh_vuc"]:
            value = document_dto.__getattribute__(field)

            if isinstance(value, str):
                document_dto.__setattr__(field, value.lower().strip())
        
        for field in ["ngay_ban_hanh", "ngay_co_hieu_luc", "ngay_het_han"]:
            value = document_dto.__getattribute__(field)

            if isinstance(value, str):
                document_dto.__setattr__(field, format_date(input=value, format="%Y-%m-%d"))
        
        if len(document_dto.co_quan_ban_hanh) > 0:
            document_dto.co_quan_ban_hanh = [item.lower().strip() for item in document_dto.co_quan_ban_hanh]
        
        return document_dto
    except Exception:
        raise
    finally:
        logger.info(f"{time.time() - start_time} s")
    