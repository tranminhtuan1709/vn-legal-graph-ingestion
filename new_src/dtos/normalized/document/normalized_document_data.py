from pydantic import BaseModel

from normalized_document import NormalizedDocument
from normalized_big_part import NormalizedBigPart
from normalized_chapter import NormalizedChapter
from normalized_part import NormalizedPart
from normalized_mini_part import NormalizedMiniPart
from normalized_article import NormalizedArticle
from normalized_article_version import NormalizedArticleVersion
from normalized_document_mapping import NormalizedDocumentMapping
from normalized_document_type import NormalizedDocumentType
from normalized_sector import NormalizedSector
from normalized_issuing_authority import NormalizedIssuingAuthority


class NormalizedDocumentData(BaseModel):
    normalized_document: NormalizedDocument
    normalized_big_parts: list[NormalizedBigPart]
    normalized_chapters: list[NormalizedChapter]
    normalized_parts: list[NormalizedPart]
    normalized_mini_parts: list[NormalizedMiniPart]
    normalized_articles: list[NormalizedArticle]
    normalized_article_versions: list[NormalizedArticleVersion]
    normalized_document_mappings: list[NormalizedDocumentMapping]
    normalized_document_type: NormalizedDocumentType
    normalized_sector: NormalizedSector
    normalized_issuing_authorities: list[NormalizedIssuingAuthority]
    