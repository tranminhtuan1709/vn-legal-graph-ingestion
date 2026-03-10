from pydantic import BaseModel

from document.document_dto import DocumentDto
from document.big_part_dto import BigPartDto
from document.chapter_dto import ChapterDto
from document.part_dto import PartDto
from document.mini_part_dto import MiniPartDto
from document.article_dto import ArticleDto
from document.article_version_dto import ArticleVersionDto
from document.document_mapping_dto import DocumentMappingDto


class DocumentData(BaseModel):
    document_dto: DocumentDto
    big_part_dtos: list[BigPartDto]
    chapter_dtos: list[ChapterDto]
    part_dtos: list[PartDto]
    mini_part_dtos: list[MiniPartDto]
    article_dtos: list[ArticleDto]
    article_version_dtos: list[ArticleVersionDto]
    document_mapping_dtos: list[DocumentMappingDto]
    