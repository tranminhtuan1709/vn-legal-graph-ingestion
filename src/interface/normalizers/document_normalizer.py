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


class DocumentNormalizer:
    def normalize_document_dto(self, dto: DocumentDto) -> DocumentDto:
        return DocumentDto(
            id=dto.id,
            so_ky_hieu=dto.so_ky_hieu if dto.so_ky_hieu not in (None, "") else None,
            ten_hien_thi=dto.ten_hien_thi if dto.ten_hien_thi not in (None, "") else None,
            ngay_ban_hanh=dto.ngay_ban_hanh if dto.ngay_ban_hanh not in (None, "") else None,
            ngay_co_hieu_luc=dto.ngay_co_hieu_luc if dto.ngay_co_hieu_luc not in (None, "") else None,
            ngay_het_han=dto.ngay_het_han if dto.ngay_het_han not in (None, "") else None,
            trang_thai=dto.trang_thai if dto.trang_thai not in (None, "") else None,
            chu_thich_nho=dto.chu_thich_nho if dto.chu_thich_nho not in (None, "") else None,
            loai_van_ban=dto.loai_van_ban if dto.loai_van_ban not in (None, "") else None,
            id_loai_van_ban=dto.id_loai_van_ban,
            linh_vuc=dto.linh_vuc if dto.linh_vuc not in (None, "") else None,
            id_linh_vuc=dto.id_linh_vuc,
            co_quan_ban_hanh=dto.co_quan_ban_hanh,
            id_co_quan_ban_hanh=dto.id_co_quan_ban_hanh
        )
            
    def normalize_big_part_dto(self, dto: BigPartDto) -> BigPartDto:
        return BigPartDto(
            id=dto.id,
            vbpl_id=dto.vbpl_id,
            big_part_number=dto.big_part_number if dto.big_part_name not in (None, "") else None,
            big_part_name=dto.big_part_name if dto.big_part_name not in (None, "") else None
        )

    def normalize_chapter_dto(self, dto: ChapterDto) -> ChapterDto:
        return ChapterDto(
            id=dto.id,
            vbpl_id=dto.vbpl_id,
            vbpl_big_part_id=dto.vbpl_big_part_id,
            chapter_number=dto.chapter_number if dto.chapter_number not in (None, "") else None,
            chapter_name=dto.chapter_name if dto.chapter_name not in (None, "") else None
        )


    def normalize_part_dto(self, dto: PartDto) -> PartDto:
        return PartDto(
            id=dto.id,
            vbpl_id=dto.vbpl_id,
            vbpl_chapter_id=dto.vbpl_chapter_id,
            part_number=dto.part_number if dto.part_number not in (None, "") else None,
            part_name=dto.part_name if dto.part_name not in (None, "") else None
        )


    def normalize_mini_part_dto(self, dto: MiniPartDto) -> MiniPartDto:
        return MiniPartDto(
            id=dto.id,
            vbpl_id=dto.vbpl_id,
            vbpl_part_id=dto.vbpl_part_id,
            mini_part_number=dto.mini_part_number if dto.mini_part_number not in (None, "") else None,
            mini_part_name=dto.mini_part_name if dto.mini_part_name not in (None, "") else None
        )


    def normalize_article_dto(self, dto: ArticleDto) -> ArticleDto:
        return ArticleDto(
            id=dto.id,
            vbpl_id=dto.vbpl_id,
            vbpl_big_part_id=dto.vbpl_big_part_id,
            vbpl_chapter_id=dto.vbpl_chapter_id,
            vbpl_part_id=dto.vbpl_part_id,
            vbpl_mini_part_id=dto.vbpl_mini_part_id,
            section_number=dto.section_number if dto.section_content not in (None, "") else None,
            section_name=dto.section_name if dto.section_name not in (None, "") else None,
            section_content=dto.section_content if dto.section_content not in (None, "") else None,
            so_phu_luc=dto.so_phu_luc if dto.so_phu_luc not in (None, "") else None,
            effective_date=dto.effective_date if dto.effective_date not in (None, "") else None
        )


    def normalize_article_version_dto(self, dto: ArticleVersionDto) -> ArticleVersionDto:
        return ArticleVersionDto(
            version_id=dto.version_id,
            vbplsd_id=dto.vbplsd_id,
            vbpldsd_id=dto.vbpldsd_id,
            dieu_sd_id=dto.dieu_sd_id,
            dieu_dsd_id=dto.dieu_dsd_id,
            phu_luc_sd=dto.phu_luc_sd if dto.phu_luc_sd not in (None, "") else None,
            phu_luc_dsd=dto.phu_luc_dsd if dto.phu_luc_dsd not in (None, "") else None,
            loai_vb=dto.loai_vb,
            bai_bo_noi_dung_truoc=dto.bai_bo_noi_dung_truoc,
            noi_dung_sua_doi=dto.noi_dung_sua_doi if dto.noi_dung_sua_doi not in (None, "") else None
        )


    def normalize_document_mapping_dto(self, dto: DocumentMappingDto) -> DocumentMappingDto:
        return dto


    def normalize_document_type_dto(self, dto: DocumentTypeDto) -> DocumentTypeDto:
        return dto


    def normalize_issuing_authority_dto(self, dto: IssuingAuthorityDto) -> IssuingAuthorityDto:
        return dto


    def normalize_sector_dto(self, dto: SectorDto) -> SectorDto:
        return dto
