import time

from interface.dtos.external.document.document_dto import DocumentDto
from interface.dtos.external.document.big_part_dto import BigPartDto
from interface.dtos.external.document.chapter_dto import ChapterDto
from interface.dtos.external.document.part_dto import PartDto
from interface.dtos.external.document.mini_part_dto import MiniPartDto
from interface.dtos.external.document.article_dto import ArticleDto
from interface.dtos.external.document.article_version_dto import ArticleVersionDto
from interface.dtos.external.document.document_mapping_dto import DocumentMappingDto
from interface.dtos.external.document.document_type_dto import DocumentTypeDto
from interface.dtos.external.document.issuing_authority_dto import IssuingAuthorityDto
from interface.dtos.external.document.sector_dto import SectorDto

from utils.datetime_utils import check_valid_date
from utils.logger import logger


class DocumentValidator:
    def validate_document_dto(self, dto: DocumentDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.so_ky_hieu is not None and not isinstance(dto.so_ky_hieu, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.so_ky_hieu: "
                f"{dto.so_ky_hieu} ({type(dto.so_ky_hieu)})"
            )

        if dto.ten_hien_thi is not None and not isinstance(dto.ten_hien_thi, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.ten_hien_thi: "
                f"{dto.ten_hien_thi} ({type(dto.ten_hien_thi)})"
            )

        if dto.ngay_ban_hanh is not None and not isinstance(dto.ngay_ban_hanh, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.ngay_ban_hanh: "
                f"{dto.ngay_ban_hanh} ({type(dto.ngay_ban_hanh)})"
            )
        
        if dto.ngay_ban_hanh is not None and not check_valid_date(date_string=dto.ngay_ban_hanh, format="%Y-%m-%d"):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid date format of DocumentDto.ngay_ban_hanh: "
                f"{dto.ngay_ban_hanh} ({type(dto.ngay_ban_hanh)})"
            )

        if dto.ngay_co_hieu_luc is not None and not isinstance(dto.ngay_co_hieu_luc, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.ngay_co_hieu_luc: {dto.ngay_co_hieu_luc} ({type(dto.ngay_co_hieu_luc)})"
                f"{dto.ngay_co_hieu_luc} ({type(dto.ngay_co_hieu_luc)})"
            )
        
        if (dto.ngay_co_hieu_luc is not None and
            not check_valid_date(date_string=dto.ngay_co_hieu_luc, format="%Y-%m-%d")):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid date format of DocumentDto.ngay_co_hieu_luc: "
                f"{dto.ngay_co_hieu_luc} ({type(dto.ngay_co_hieu_luc)})"
            )

        if dto.ngay_het_han is not None and not isinstance(dto.ngay_het_han, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.ngay_het_han: {dto.ngay_het_han} ({type(dto.ngay_het_han)})"
                f"{dto.ngay_het_han} ({type(dto.ngay_het_han)})"
            )
        
        if dto.ngay_het_han is not None and not check_valid_date(date_string=dto.ngay_het_han, format="%Y-%m-%d"):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid date format of DocumentDto.ngay_het_han: "
                f"{dto.ngay_het_han} ({type(dto.ngay_het_han)})"
            )

        if dto.trang_thai is not None and not isinstance(dto.trang_thai, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.trang_thai: "
                f"{dto.trang_thai} ({type(dto.trang_thai)})"
            )

        if dto.chu_thich_nho is not None and not isinstance(dto.chu_thich_nho, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.chu_thich_nho: "
                f"{dto.chu_thich_nho} ({type(dto.chu_thich_nho)})"
            )

        if dto.loai_van_ban is not None and not isinstance(dto.loai_van_ban, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.loai_van_ban: "
                f"{dto.loai_van_ban} ({type(dto.loai_van_ban)})"
            )

        if dto.linh_vuc is not None and not isinstance(dto.linh_vuc, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.linh_vuc: "
                f"{dto.linh_vuc} ({type(dto.linh_vuc)})"
            )

        if dto.id_loai_van_ban is not None and not isinstance(dto.id_loai_van_ban, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.id_loai_van_ban: "
                f"{dto.id_loai_van_ban} ({type(dto.id_loai_van_ban)})"
            )

        if dto.id_linh_vuc is not None and not isinstance(dto.id_linh_vuc, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.id_linh_vuc: "
                f"{dto.id_linh_vuc} ({type(dto.id_linh_vuc)})"
            )

        if dto.co_quan_ban_hanh is None or not isinstance(dto.co_quan_ban_hanh, list):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.co_quan_ban_hanh:"
                f"{dto.co_quan_ban_hanh} ({type(dto.co_quan_ban_hanh)})"
            )

        for item in dto.co_quan_ban_hanh:
            if not isinstance(item, str):
                logger.info(msg=f"{round(time.time() - start_time, 4)} s")
                
                raise ValueError(
                    f"Invalid value of DocumentDto.co_quan_ban_hanh item: "
                    f"{item} ({type(item)})"
                )

        if dto.id_co_quan_ban_hanh is None or not isinstance(dto.id_co_quan_ban_hanh, list):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentDto.id_co_quan_ban_hanh: "
                f"{dto.id_co_quan_ban_hanh} ({type(dto.id_co_quan_ban_hanh)})"
            )

        for item in dto.id_co_quan_ban_hanh:
            if not isinstance(item, int):
                logger.info(msg=f"{round(time.time() - start_time, 4)} s")
                
                raise ValueError(
                    f"Invalid value of DocumentDto.id_co_quan_ban_hanh item: "
                    f"{item} ({type(item)})"
                )

    def validate_big_part_dto(self, dto: BigPartDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of BigPartDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of BigPartDto.vbpl_id: "
                f"{dto.vbpl_id} ({type(dto.vbpl_id)})"
            )

        if dto.big_part_number is not None and not isinstance(dto.big_part_number, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of BigPartDto.big_part_number: "
                f"{dto.big_part_number} ({type(dto.big_part_number)})"
            )

        if dto.big_part_name is not None and not isinstance(dto.big_part_name, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of BigPartDto.big_part_name: "
                f"{dto.big_part_name} ({type(dto.big_part_name)})"
            )

    def validate_chapter_dto(self, dto: ChapterDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ChapterDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ChapterDto.vbpl_id: "
                f"{dto.vbpl_id} ({type(dto.vbpl_id)})"
            )

        if dto.vbpl_big_part_id is not None and not isinstance(dto.vbpl_big_part_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ChapterDto.vbpl_big_part_id: "
                f"{dto.vbpl_big_part_id} ({type(dto.vbpl_big_part_id)})"
            )

        if dto.chapter_number is not None and not isinstance(dto.chapter_number, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ChapterDto.chapter_number: "
                f"{dto.chapter_number} ({type(dto.chapter_number)})"
            )

        if dto.chapter_name is not None and not isinstance(dto.chapter_name, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ChapterDto.chapter_name: "
                f"{dto.chapter_name} ({type(dto.chapter_name)})"
            )

    def validate_part_dto(self, dto: PartDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of PartDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of PartDto.vbpl_id: "
                f"{dto.vbpl_id} ({type(dto.vbpl_id)})"
            )

        if dto.vbpl_chapter_id is not None and not isinstance(dto.vbpl_chapter_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of PartDto.vbpl_chapter_id: "
                f"{dto.vbpl_chapter_id} ({type(dto.vbpl_chapter_id)})"
            )

        if dto.part_number is not None and not isinstance(dto.part_number, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of PartDto.part_number: "
                f"{dto.part_number} ({type(dto.part_number)})"
            )

        if dto.part_name is not None and not isinstance(dto.part_name, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of PartDto.part_name: "
                f"{dto.part_name} ({type(dto.part_name)})"
            )

    def validate_mini_part_dtos(self, dto: MiniPartDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of MiniPartDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of MiniPartDto.vbpl_id: "
                f"{dto.vbpl_id} ({type(dto.vbpl_id)})"
            )

        if dto.vbpl_part_id is not None and not isinstance(dto.vbpl_part_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of MiniPartDto.vbpl_part_id: "
                f"{dto.vbpl_part_id} ({type(dto.vbpl_part_id)})"
            )

        if dto.mini_part_number is not None and not isinstance(dto.mini_part_number, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of MiniPartDto.mini_part_number: "
                f"{dto.mini_part_number} ({type(dto.mini_part_number)})"
            )

        if dto.mini_part_name is not None and not isinstance(dto.mini_part_name, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of MiniPartDto.mini_part_name: "
                f"{dto.mini_part_name} ({type(dto.mini_part_name)})"
            )

    def validate_article_dto(self, dto: ArticleDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.vbpl_id: "
                f"{dto.vbpl_id} ({type(dto.vbpl_id)})"
            )

        if dto.vbpl_big_part_id is not None and not isinstance(dto.vbpl_big_part_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.vbpl_big_part_id: "
                f"{dto.vbpl_big_part_id} ({type(dto.vbpl_big_part_id)})"
            )

        if dto.vbpl_chapter_id is not None and not isinstance(dto.vbpl_chapter_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.vbpl_chapter_id: "
                f"{dto.vbpl_chapter_id} ({type(dto.vbpl_chapter_id)})"
            )

        if dto.vbpl_part_id is not None and not isinstance(dto.vbpl_part_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.vbpl_part_id: "
                f"{dto.vbpl_part_id} ({type(dto.vbpl_part_id)})"
            )

        if dto.vbpl_mini_part_id is not None and not isinstance(dto.vbpl_mini_part_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.vbpl_mini_part_id: "
                f"{dto.vbpl_mini_part_id} ({type(dto.vbpl_mini_part_id)})"
            )

        if dto.section_number is not None and not isinstance(dto.section_number, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.section_number: "
                f"{dto.section_number} ({type(dto.section_number)})"
            )

        if dto.section_name is not None and not isinstance(dto.section_name, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.section_name: "
                f"{dto.section_name} ({type(dto.section_name)})"
            )

        if dto.section_content is not None and not isinstance(dto.section_content, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.section_content: "
                f"{dto.section_content} ({type(dto.section_content)})"
            )

        if dto.so_phu_luc is not None and not isinstance(dto.so_phu_luc, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.so_phu_luc: "
                f"{dto.so_phu_luc} ({type(dto.so_phu_luc)})"
            )

        if dto.effective_date is not None and not isinstance(dto.effective_date, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleDto.effective_date: "
                f"{dto.effective_date} ({type(dto.effective_date)})"
            )

        if dto.effective_date is not None and not check_valid_date(date_string=dto.effective_date, format="%Y-%m-%d"):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid date format of ArticleDto.effective_date: "
                f"{dto.effective_date} ({type(dto.effective_date)})"
            )

    def validate_article_version_dto(self, dto: ArticleVersionDto) -> None:
        start_time = time.time()

        if dto.version_id is None or not isinstance(dto.version_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.version_id: "
                f"{dto.version_id} ({type(dto.version_id)})"
            )

        if dto.vbplsd_id is None or not isinstance(dto.vbplsd_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.vbplsd_id: "
                f"{dto.vbplsd_id} ({type(dto.vbplsd_id)})"
            )

        if dto.vbpldsd_id is None or not isinstance(dto.vbpldsd_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.vbpldsd_id: "
                f"{dto.vbpldsd_id} ({type(dto.vbpldsd_id)})"
            )

        if dto.dieu_sd in ("", None) or not isinstance(dto.dieu_sd, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.dieu_sd: "
                f"{dto.dieu_sd} ({type(dto.dieu_sd)})"
            )

        if dto.dieu_dsd in ("", None) or not isinstance(dto.dieu_dsd, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.dieu_dsd: "
                f"{dto.dieu_dsd} ({type(dto.dieu_dsd)})"
            )

        if dto.dieu_sd_id is None or not isinstance(dto.dieu_sd_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.dieu_sd_id: "
                f"{dto.dieu_sd_id} ({type(dto.dieu_sd_id)})"
            )

        if dto.dieu_dsd_id is None or not isinstance(dto.dieu_dsd_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.dieu_dsd_id: "
                f"{dto.dieu_dsd_id} ({type(dto.dieu_dsd_id)})"
            )

        if dto.phu_luc_dsd is not None and not isinstance(dto.phu_luc_dsd, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.phu_luc_dsd: "
                f"{dto.phu_luc_dsd} ({type(dto.phu_luc_dsd)})"
            )

        if not isinstance(dto.loai_vb, str) or dto.loai_vb in (None, "") or dto.loai_vb not in ("SĐ", "BS", "NHL"):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.loai_vb: "
                f"{dto.loai_vb} ({type(dto.loai_vb)})"
            )

        if dto.from_date is not None and not isinstance(dto.from_date, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.from_date: "
                f"{dto.from_date} ({type(dto.from_date)})"
            )

        if dto.from_date is not None and not check_valid_date(date_string=dto.from_date, format="%Y-%m-%d"):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid date format of ArticleVersionDto.from_date: "
                f"{dto.from_date} ({type(dto.from_date)})"
            )

        if dto.to_date is not None and not isinstance(dto.to_date, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.to_date: "
                f"{dto.to_date} ({type(dto.to_date)})"
            )

        if dto.to_date is not None and not check_valid_date(date_string=dto.to_date, format="%Y-%m-%d"):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid date format of ArticleVersionDto.to_date: "
                f"{dto.to_date} ({type(dto.to_date)})"
            )

        if dto.bai_bo_noi_dung_truoc is not None and not isinstance(dto.bai_bo_noi_dung_truoc, bool):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.bai_bo_noi_dung_truoc: "
                f"{dto.bai_bo_noi_dung_truoc} ({type(dto.bai_bo_noi_dung_truoc)})"
            )

        if dto.noi_dung_sua_doi is not None and not isinstance(dto.noi_dung_sua_doi, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of ArticleVersionDto.noi_dung_sua_doi: "
                f"{dto.noi_dung_sua_doi} ({type(dto.noi_dung_sua_doi)})"
            )

    def validate_document_mapping_dto(self, dto: DocumentMappingDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentMappingDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.from_document_id is None or not isinstance(dto.from_document_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentMappingDto.from_document_id: "
                f"{dto.from_document_id} ({type(dto.from_document_id)})"
            )

        if dto.to_document_id is None or not isinstance(dto.to_document_id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentMappingDto.to_document_id: "
                f"{dto.to_document_id} ({type(dto.to_document_id)})"
            )

        if (dto.relationship_type is None or
            not isinstance(dto.relationship_type, str) or
            dto.relationship_type not in ("huong_dan", "sua_doi", "thay_the", "dinh_chinh", "hop_nhat")
        ):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentMappingDto.relationship_type: "
                f"{dto.relationship_type} ({type(dto.relationship_type)})"
            )

    def validate_document_type_dto(self, dto: DocumentTypeDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentTypeDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.loai_van_ban is None or not isinstance(dto.loai_van_ban, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of DocumentTypeDto.loai_van_ban: "
                f"{dto.loai_van_ban} ({type(dto.loai_van_ban)})"
            )

    def validate_issuing_authority_dto(self, dto: IssuingAuthorityDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of IssuingAuthorityDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.co_quan_ban_hanh is None or not isinstance(dto.co_quan_ban_hanh, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of IssuingAuthorityDto.co_quan_ban_hanh: "
                f"{dto.co_quan_ban_hanh} ({type(dto.co_quan_ban_hanh)})"
            )

    def validate_sector_dto(self, dto: SectorDto) -> None:
        start_time = time.time()

        if dto.id is None or not isinstance(dto.id, int):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of SectorDto.id: "
                f"{dto.id} ({type(dto.id)})"
            )

        if dto.linh_vuc is None or not isinstance(dto.linh_vuc, str):
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
            
            raise ValueError(
                f"Invalid value of SectorDto.linh_vuc: "
                f"{dto.linh_vuc} ({type(dto.linh_vuc)})"
            )
