from pydantic import BaseModel

from validated_document import ValidatedDocument
from validated_big_part import ValidatedBigPart
from validated_chapter import ValidatedChapter
from validated_part import ValidatedPart
from validated_mini_part import ValidatedMiniPart
from validated_article import ValidatedArticle
from validated_article_version import ValidatedArticleVersion
from validated_document_mapping import ValidatedDocumentMapping
from validated_document_type import ValidatedDocumentType
from validated_sector import ValidatedSector
from validated_issuing_authority import ValidatedIssuingAuthority


class ValidatedDocumentData(BaseModel):
    validated_document: ValidatedDocument
    validated_big_parts: list[ValidatedBigPart]
    validated_chapters: list[ValidatedChapter]
    validated_parts: list[ValidatedPart]
    validated_mini_parts: list[ValidatedMiniPart]
    validated_articles: list[ValidatedArticle]
    validated_article_versions: list[ValidatedArticleVersion]
    validated_document_mappings: list[ValidatedDocumentMapping]
    validated_document_type: ValidatedDocumentType
    validated_sector: ValidatedSector
    validated_issuing_authorities: list[ValidatedIssuingAuthority]
    