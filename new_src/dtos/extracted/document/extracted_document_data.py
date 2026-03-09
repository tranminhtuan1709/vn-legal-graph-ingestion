from pydantic import BaseModel

from extracted_document import ExtractedDocument
from extracted_big_part import ExtractedBigPart
from extracted_chapter import ExtractedChapter
from extracted_part import ExtractedPart
from extracted_mini_part import ExtractedMiniPart
from extracted_article import ExtractedArticle
from extracted_article_version import ExtractedArticleVersion
from extracted_document_mapping import ExtractedDocumentMapping
from extracted_document_type import ExtractedDocumentType
from extracted_sector import ExtractedSector
from extracted_issuing_authority import ExtractedIssuingAuthority


class ExtractedDocumentData(BaseModel):
    extracted_document: ExtractedDocument
    extracted_big_parts: list[ExtractedBigPart]
    extracted_chapters: list[ExtractedChapter]
    extracted_parts: list[ExtractedPart]
    extracted_mini_parts: list[ExtractedMiniPart]
    extracted_articles: list[ExtractedArticle]
    extracted_article_versions: list[ExtractedArticleVersion]
    extracted_document_mappings: list[ExtractedDocumentMapping]
    extracted_document_type: ExtractedDocumentType
    extracted_sector: ExtractedSector
    extracted_issuing_authorities: list[ExtractedIssuingAuthority]
    