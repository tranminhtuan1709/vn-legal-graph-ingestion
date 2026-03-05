from ..dtos.external.documents.document_dto import DocumentDto
from ..dtos.external.documents.big_part_dto import BigPartDto
from ..dtos.external.documents.chapter_dto import ChapterDto
from ..dtos.external.documents.part_dto import PartDto
from ..dtos.external.documents.mini_part_dto import MiniPartDto
from ..dtos.external.documents.article_dto import ArticleDto
from ..dtos.external.documents.article_version_dto import ArticleVersionDto
from ..dtos.external.documents.document_mapping_dto import DocumentMappingDto
from ..dtos.external.documents.document_type_dto import DocumentTypeDto
from ..dtos.external.documents.issuing_authority_dto import IssuingAuthorityDto
from ..dtos.external.documents.sector_dto import SectorDto

from ...exceptions.custom_exceptions import ValidationError
from ...utils.datetime_utils import check_valid_date


class DocumentValidator:
    def validate_document_dto(self, dto: DocumentDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of DocumentDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )

        if dto.so_ky_hieu is not None and not isinstance(dto.so_ky_hieu, str):
            raise ValidationError(
                message="Invalid data type of DocumentDto.so_ky_hieu",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.so_ky_hieu)
                }
            )
        
        if dto.ten_hien_thi is not None and not isinstance(dto.ten_hien_thi, str):
            raise ValidationError(
                message="Invalid data type of DocumentDto.ten_hien_thi",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.ten_hien_thi)
                }
            )

        if dto.ngay_ban_hanh is not None and not isinstance(dto.ngay_ban_hanh, str):
            raise ValidationError(
                message="Invalid data type of DocumentDto.ngay_ban_hanh",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.ngay_ban_hanh)
                }
            )

        if dto.ngay_co_hieu_luc is not None and not isinstance(dto.ngay_co_hieu_luc, str):
            raise ValidationError(
                message="Invalid data type of DocumentDto.ngay_co_hieu_luc",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.ngay_co_hieu_luc)
                }
            )

        if dto.ngay_het_han is not None and not isinstance(dto.ngay_het_han, str):
            raise ValidationError(
                message="Invalid data type of DocumentDto.ngay_het_han",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.ngay_het_han)
                }
            )

        if dto.trang_thai is not None and not isinstance(dto.trang_thai, str):
            raise ValidationError(
                message="Invalid data type of DocumentDto.trang_thai",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.trang_thai)
                }
            )

        if dto.chu_thich_nho is not None and not isinstance(dto.chu_thich_nho, str):
            raise ValidationError(
                message="Invalid data type of DocumentDto.chu_thich_nho",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.chu_thich_nho)
                }
            )

        if dto.loai_van_ban is not None and not isinstance(dto.loai_van_ban, str):
            raise ValidationError(
                message="Invalid data type of DocumentDto.loai_van_ban",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.loai_van_ban)
                }
            )

        if dto.linh_vuc is not None and not isinstance(dto.linh_vuc, str):
            raise ValidationError(
                message="Invalid data type of DocumentDto.linh_vuc",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.linh_vuc)
                }
            )

        if dto.id_loai_van_ban is not None and not isinstance(dto.id_loai_van_ban, int):
            raise ValidationError(
                message="Invalid data type of DocumentDto.id_loai_van_ban",
                context={
                    "expected_type": "int",
                    "invalid_type": type(dto.id_loai_van_ban)
                }
            )

        if dto.id_linh_vuc is not None and not isinstance(dto.id_linh_vuc, int):
            raise ValidationError(
                message="Invalid data type of DocumentDto.id_linh_vuc",
                context={
                    "expected_type": "int",
                    "invalid_type": type(dto.id_linh_vuc)
                }
            )

        if dto.co_quan_ban_hanh is None or not isinstance(dto.co_quan_ban_hanh, list):
            raise ValidationError(
                message="DocumentDto.co_quan_ban_hanh must be a list",
                context={
                    "expected_type": "list",
                    "invalid_type": type(dto.co_quan_ban_hanh)
                }
            )

        for item in dto.co_quan_ban_hanh:
            if not isinstance(item, str):
                raise ValidationError(
                    message="Invalid data type of an item in DocumentDto.co_quan_ban_hanh",
                    context={
                        "expected_type": "str",
                        "invalid_type": type(item)
                    }
                )
        
        if dto.id_co_quan_ban_hanh is None or not isinstance(dto.id_co_quan_ban_hanh, list):
            raise ValidationError(
                message="DocumentDto.id_co_quan_ban_hanh must be a list",
                context={
                    "expected_type": "list",
                    "invalid_type": type(dto.id_co_quan_ban_hanh)
                }
            )

        for item in dto.id_co_quan_ban_hanh:
            if not isinstance(item, int):
                raise ValidationError(
                    message="Invalid data type of an item in DocumentDto.id_co_quan_ban_hanh",
                    context={
                        "expected_type": "int",
                        "invalid_type": type(item)
                    }
                )
    
    def validate_big_part_dto(self, dto: BigPartDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of BigPartDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )

        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            raise ValidationError(
                message="Invalid value of BigPartDto.vbpl_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.vbpl_id
                }
            )
        
        if dto.big_part_number is not None and not isinstance(dto.big_part_number, str):
            raise ValidationError(
                message="Invalid data type of BigPartDto.big_part_number",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.big_part_number)
                }
            )
        
        if dto.big_part_name is not None and not isinstance(dto.big_part_name, str):
            raise ValidationError(
                message="Invalid data type of BigPartDto.big_part_name",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.big_part_name)
                }
            )
    
    def validate_chapter_dto(self, dto: ChapterDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of ChapterDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )

        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            raise ValidationError(
                message="Invalid value of ChapterDto.vbpl_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.vbpl_id
                }
            )

        if dto.vbpl_big_part_id is not None and not isinstance(dto.vbpl_big_part_id, int):
            raise ValidationError(
                message="Invalid data type of ChapterDto.vbpl_big_part_id",
                context={
                    "expected_type": "int",
                    "invalid_type": type(dto.vbpl_big_part_id)
                }
            )
        
        if dto.chapter_number is not None and not isinstance(dto.chapter_number, str):
            raise ValidationError(
                message="Invalid data type of ChapterDto.chapter_number",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.chapter_number)
                }
            )
        
        if dto.chapter_name is not None and not isinstance(dto.chapter_name, str):
            raise ValidationError(
                message="Invalid data type of ChapterDto.chapter_name",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.chapter_name)
                }
            )
    
    def validate_part_dto(self, dto: PartDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of PartDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )

        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            raise ValidationError(
                message="Invalid value of PartDto.vbpl_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.vbpl_id
                }
            )

        if dto.vbpl_chapter_id is not None and not isinstance(dto.vbpl_chapter_id, int):
            raise ValidationError(
                message="Invalid data type of PartDto.vbpl_chapter_id",
                context={
                    "expected_type": "int",
                    "invalid_type": type(dto.vbpl_chapter_id)
                }
            )
        
        if dto.part_number is not None and not isinstance(dto.part_number, str):
            raise ValidationError(
                message="Invalid data type of PartDto.part_number",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.part_number)
                }
            )
        
        if dto.part_name is not None and not isinstance(dto.part_name, str):
            raise ValidationError(
                message="Invalid data type of PartDto.part_name",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.part_name)
                }
            )
    
    def validate_mini_part_dtos(self, dto: MiniPartDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of MiniPartDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )

        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            raise ValidationError(
                message="Invalid value of MiniPartDto.vbpl_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.vbpl_id
                }
            )

        if dto.vbpl_part_id is not None and not isinstance(dto.vbpl_part_id, int):
            raise ValidationError(
                message="Invalid data type of MiniPartDto.vbpl_part_id",
                context={
                    "expected_type": "int",
                    "invalid_type": type(dto.vbpl_part_id)
                }
            )
        
        if dto.mini_part_number is not None and not isinstance(dto.mini_part_number, str):
            raise ValidationError(
                message="Invalid data type of MiniPartDto.mini_part_number",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.mini_part_number)
                }
            )
        
        if dto.mini_part_name is not None and not isinstance(dto.mini_part_name, str):
            raise ValidationError(
                message="Invalid data type of MiniPartDto.mini_part_name",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.mini_part_name)
                }
            )
    
    def validate_article_dto(self, dto: ArticleDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of ArticleDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )
        
        if dto.vbpl_id is None or not isinstance(dto.vbpl_id, int):
            raise ValidationError(
                message="Invalid value of ArticleDto.vbpl_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.vbpl_id
                }
            )
        
        if dto.vbpl_big_part_id is not None and not isinstance(dto.vbpl_big_part_id, int):
            raise ValidationError(
                message="Invalid data type of ArticleDto.vbpl_big_part_id",
                context={
                    "expected_type": "int",
                    "invalid_type": type(dto.vbpl_big_part_id)
                }
            )
        
        if dto.vbpl_chapter_id is not None and not isinstance(dto.vbpl_chapter_id, int):
            raise ValidationError(
                message="Invalid data type of ArticleDto.vbpl_chapter_id",
                context={
                    "expected_type": "int",
                    "invalid_type": type(dto.vbpl_chapter_id)
                }
            )
        
        if dto.vbpl_part_id is not None and not isinstance(dto.vbpl_part_id, int):
            raise ValidationError(
                message="Invalid data type of ArticleDto.vbpl_part_id",
                context={
                    "expected_type": "int",
                    "invalid_type": type(dto.vbpl_part_id)
                }
            )
        
        if dto.vbpl_mini_part_id is not None and not isinstance(dto.vbpl_mini_part_id, int):
            raise ValidationError(
                message="Invalid data type of ArticleDto.vbpl_mini_part_id",
                context={
                    "expected_type": "int",
                    "invalid_type": type(dto.vbpl_mini_part_id)
                }
            )
        
        if dto.section_number is not None and not isinstance(dto.section_number, str):
            raise ValidationError(
                message="Invalid data type of ArticleDto.section_number",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.section_number)
                }
            )
        
        if dto.section_name is not None and not isinstance(dto.section_name, str):
            raise ValidationError(
                message="Invalid data type of ArticleDto.section_name",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.section_name)
                }
            )
        
        if dto.section_content is not None and not isinstance(dto.section_content, str):
            raise ValidationError(
                message="Invalid data type of ArticleDto.section_content",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.section_content)
                }
            )
        
        if dto.so_phu_luc is not None and not isinstance(dto.so_phu_luc, str):
            raise ValidationError(
                message="Invalid data type of ArticleDto.so_phu_luc",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.so_phu_luc)
                }
            )

        if dto.effective_date is not None and not isinstance(dto.effective_date, str):
            raise ValidationError(
                message="Invalid data type of ArticleDto.effective_date",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.effective_date)
                }
            )
        
        if isinstance(dto.effective_date, str) and not check_valid_date(date_string=dto.effective_date, format="%Y-%m-%d"):
            raise ValidationError(
                message="Invalid value of ArticleDto.effective_date",
                context={
                    "expected_value": "yyyy-mm-dd",
                    "invalid_value": dto.effective_date
                }
            )
    
    def validate_article_version_dto(self, dto: ArticleVersionDto) -> None:
        if dto.version_id is None or not isinstance(dto.version_id, int):
            raise ValidationError(
                message="Invalid value of ArticleVersionDto.version_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.version_id
                }
            )
        
        if dto.vbplsd_id is None or not isinstance(dto.vbplsd_id, int):
            raise ValidationError(
                message="Invalid value of ArticleVersionDto.vbplsd_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.vbplsd_id
                }
            )
        
        if dto.vbpldsd_id is None or not isinstance(dto.vbpldsd_id, int):
            raise ValidationError(
                message="Invalid value of ArticleVersionDto.vbpldsd_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.vbpldsd_id
                }
            )
        
        if dto.dieu_sd_id is None or not isinstance(dto.dieu_sd_id, int):
            raise ValidationError(
                message="Invalid value of ArticleVersionDto.dieu_sd_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.dieu_sd_id
                }
            )
        
        if dto.dieu_dsd_id is None or not isinstance(dto.dieu_dsd_id, int):
            raise ValidationError(
                message="Invalid value of ArticleVersionDto.dieu_dsd_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.dieu_dsd_id
                }
            )
        
        if dto.phu_luc_dsd is not None and not isinstance(dto.phu_luc_dsd, str):
            raise ValidationError(
                message="Invalid data type of ArticleVersionDto.phu_luc_dsd",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.phu_luc_dsd)
                }
            )

        if not isinstance(dto.loai_vb, str) or dto.loai_vb in (None, ""):
            raise ValidationError(
                message="Invalid value of ArticleVersionDto.loai_vb",
                context={
                    "expected_value": "str",
                    "invalid_value": dto.loai_vb
                }
            )
        
        if dto.from_date is not None and not isinstance(dto.from_date, str):
            raise ValidationError(
                message="Invalid data type of ArticleVersionDto.from_date",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.from_date)
                }
            )
        
        if isinstance(dto.from_date, str) and not check_valid_date(date_string=dto.from_date, format="%Y-%m-%d"):
            raise ValidationError(
                message="Invalid value of ArticleVersionDto.from_date",
                context={
                    "expected_value": "yyyy-mm-dd",
                    "invalid_value": dto.from_date
                }
            )
        
        if dto.to_date is not None and not isinstance(dto.to_date, str):
            raise ValidationError(
                message="Invalid data type of ArticleVersionDto.to_date",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.to_date)
                }
            )
        
        if isinstance(dto.to_date, str) and not check_valid_date(date_string=dto.to_date, format="%Y-%m-%d"):
            raise ValidationError(
                message="Invalid value of ArticleVersionDto.to_date",
                context={
                    "expected_value": "yyyy-mm-dd",
                    "invalid_value": dto.to_date
                }
            )
        
        if dto.bai_bo_noi_dung_truoc is not None and not isinstance(dto.bai_bo_noi_dung_truoc, bool):
            raise ValidationError(
                message="Invalid data type of ArticleVersionDto.bai_bo_noi_dung_truoc",
                context={
                    "expected_type": "bool",
                    "invalid_type": type(dto.bai_bo_noi_dung_truoc)
                }
            )
        
        if dto.noi_dung_sua_doi is not None and not isinstance(dto.noi_dung_sua_doi, str):
            raise ValidationError(
                message="Invalid data type of ArticleVersionDto.noi_dung_sua_doi",
                context={
                    "expected_type": "str",
                    "invalid_type": type(dto.noi_dung_sua_doi)
                }
            )
            
    def validate_document_mapping_dto(self, dto: DocumentMappingDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of DocumentMappingDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )
        
        if dto.from_document_id is None or not isinstance(dto.from_document_id, int):
            raise ValidationError(
                message="Invalid value of DocumentMappingDto.from_document_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.from_document_id
                }
            )
        
        if dto.to_document_id is None or not isinstance(dto.to_document_id, int):
            raise ValidationError(
                message="Invalid value of DocumentMappingDto.to_document_id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.to_document_id
                }
            )
        
        if dto.relationship_type is None or not isinstance(dto.relationship_type, str):
            raise ValidationError(
                message="Invalid value of DocumentMappingDto.relationship_type",
                context={
                    "expected_value": "str",
                    "invalid_value": dto.relationship_type
                }
            )
            
    def validate_document_type_dto(self, dto: DocumentTypeDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of DocumentTypeDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )
        
        if dto.loai_van_ban is None or not isinstance(dto.loai_van_ban, str):
            raise ValidationError(
                message="Invalid value of DocumentTypeDto.loai_van_ban",
                context={
                    "expected_value": "str",
                    "invalid_value": dto.loai_van_ban
                }
            )
    
    def validate_issuing_authority_dto(self, dto: IssuingAuthorityDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of IssuingAuthorityDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )
        
        if dto.co_quan_ban_hanh is None or not isinstance(dto.co_quan_ban_hanh, str):
            raise ValidationError(
                message="Invalid value of IssuingAuthorityDto.co_quan_ban_hanh",
                context={
                    "expected_value": "str",
                    "invalid_value": dto.co_quan_ban_hanh
                }
            )
            
    def validate_sector_dto(self, dto: SectorDto) -> None:
        if dto.id is None or not isinstance(dto.id, int):
            raise ValidationError(
                message="Invalid value of SectorDto.id",
                context={
                    "expected_value": "int",
                    "invalid_value": dto.id
                }
            )
        
        if dto.linh_vuc is None or not isinstance(dto.linh_vuc, str):
            raise ValidationError(
                message="Invalid value of SectorDto.linh_vuc",
                context={
                    "expected_value": "str",
                    "invalid_value": dto.linh_vuc
                }
            )
