from src.interface.dtos.external.document.document_dto import DocumentDto
from src.interface.dtos.external.document.big_part_dto import BigPartDto
from src.interface.dtos.external.document.chapter_dto import ChapterDto
from src.interface.dtos.external.document.part_dto import PartDto
from src.interface.dtos.external.document.mini_part_dto import MiniPartDto
from src.interface.dtos.external.document.article_dto import ArticleDto
from src.interface.dtos.external.document.article_version_dto import ArticleVersionDto
from src.interface.dtos.external.document.document_mapping_dto import DocumentMappingDto
from src.interface.dtos.external.document.document_type_dto import DocumentTypeDto
from src.interface.dtos.external.document.issuing_authority_dto import IssuingAuthorityDto
from src.interface.dtos.external.document.sector_dto import SectorDto


class FetchDocumentResult:
    def __init__(
        self,
        document_dto: DocumentDto,
        big_part_dtos: list[BigPartDto],
        chapter_dtos: list[ChapterDto],
        part_dtos: list[PartDto],
        mini_part_dtos: list[MiniPartDto],
        article_dtos: list[ArticleDto],
        article_version_dtos: list[ArticleVersionDto],
        document_mapping_dtos: list[DocumentMappingDto],
        document_type_dto: DocumentTypeDto,
        issuing_authority_dtos: list[IssuingAuthorityDto],
        sector_dto: SectorDto
    ) -> None:
        self.document_dto = document_dto
        self.big_part_dtos = big_part_dtos
        self.chapter_dtos = chapter_dtos
        self.part_dtos = part_dtos
        self.mini_part_dtos = mini_part_dtos
        self.article_dtos = article_dtos
        self.article_version_dtos = article_version_dtos
        self.document_mapping_dtos = document_mapping_dtos
        self.document_type_dto = document_type_dto
        self.issuing_authority_dtos = issuing_authority_dtos
        self.sector_dto = sector_dto
