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

from utils.logger import logger


class DocumentNormalizer:
    def normalize_document_dto(self, dto: DocumentDto) -> DocumentDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_big_part_dto(self, dto: BigPartDto) -> BigPartDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_chapter_dto(self, dto: ChapterDto) -> ChapterDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_part_dto(self, dto: PartDto) -> PartDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_mini_part_dto(self, dto: MiniPartDto) -> MiniPartDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_article_dto(self, dto: ArticleDto) -> ArticleDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_article_version_dto(self, dto: ArticleVersionDto) -> ArticleVersionDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_document_mapping_dto(self, dto: DocumentMappingDto) -> DocumentMappingDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_document_type_dto(self, dto: DocumentTypeDto) -> DocumentTypeDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_issuing_authority_dto(self, dto: IssuingAuthorityDto) -> IssuingAuthorityDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto

    def normalize_sector_dto(self, dto: SectorDto) -> SectorDto:
        start_time = time.time()
        logger.info(msg=f"{round(time.time() - start_time, 4)} s")
        return dto
