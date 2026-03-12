from pydantic import BaseModel

from dtos.document.document_dto import DocumentDto
from dtos.document.big_part_dto import BigPartDto
from dtos.document.chapter_dto import ChapterDto
from dtos.document.part_dto import PartDto
from dtos.document.mini_part_dto import MiniPartDto
from dtos.document.article_dto import ArticleDto
from dtos.document.article_version_dto import ArticleVersionDto
from dtos.document.document_mapping_dto import DocumentMappingDto


class DocumentData(BaseModel):
    document_dto: DocumentDto | None
    big_part_dtos: list[BigPartDto]
    chapter_dtos: list[ChapterDto]
    part_dtos: list[PartDto]
    mini_part_dtos: list[MiniPartDto]
    article_dtos: list[ArticleDto]
    article_version_dtos: list[ArticleVersionDto]
    document_mapping_dtos: list[DocumentMappingDto]
    