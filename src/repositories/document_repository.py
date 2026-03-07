import json

from mysql.connector.abstracts import MySQLCursorAbstract

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

from src.infrastructure.mysql_client import MySQLClient
from src.exceptions.custom_exceptions import FetchDataError
from src.interface.validators.document_validator import DocumentValidator
from src.interface.normalizers.document_normalizer import DocumentNormalizer
from src.interface.dtos.internal.document.fetch_document_result import FetchDocumentResult


class DocumentRepository:
    def __init__(
        self,
        mysql_client: MySQLClient,
        document_validator: DocumentValidator,
        document_normalizer: DocumentNormalizer
    ) -> None:
        self.mysql_client = mysql_client
        self.document_validator = document_validator
        self.document_normalizer = document_normalizer

    def fetch_document_dto(self, cursor: MySQLCursorAbstract, document_id: int) -> DocumentDto:
        try:
            cursor.execute(
                operation="""
                    SELECT
                        id,
                        so_ky_hieu,
                        ten_hien_thi,
                        DATE(ngay_ban_hanh) AS ngay_ban_hanh,
                        DATE(ngay_co_hieu_luc) AS ngay_co_hieu_luc,
                        DATE(ngay_het_han) AS ngay_het_han,
                        trang_thai,
                        chu_thich_nho,
                        loai_van_ban,
                        id_loai_van_ban,
                        linh_vuc,
                        id_linh_vuc,
                        co_quan_ban_hanh,
                        id_co_quan_ban_hanh
                    FROM vbpl
                    WHERE id = %(document_id)s;
                """,
                params={
                    "document_id": document_id
                }
            )

            record = cursor.fetchone()

            dto = DocumentDto(
                id=record.get("id"),
                so_ky_hieu=record.get("so_ky_hieu"),
                ten_hien_thi=record.get("ten_hien_thi"),
                ngay_ban_hanh=record.get("ngay_ban_hanh"),
                ngay_co_hieu_luc=record.get("ngay_co_hieu_luc"),
                ngay_het_han=record.get("ngay_het_han"),
                trang_thai=record.get("trang_thai"),
                chu_thich_nho=record.get("chu_thich_nho"),
                loai_van_ban=record.get("loai_van_ban"),
                id_loai_van_ban=record.get("id_loai_van_ban"),
                linh_vuc=record.get("linh_vuc"),
                id_linh_vuc=record.get("id_linh_vuc"),
                co_quan_ban_hanh=record.get("co_quan_ban_hanh"),
                id_co_quan_ban_hanh=record.get("id_co_quan_ban_hanh"),
            )

            if dto.co_quan_ban_hanh in (None, ""):
                dto.co_quan_ban_hanh = []
            else:
                dto.co_quan_ban_hanh = dto.co_quan_ban_hanh.split(",")
            
            if dto.id_co_quan_ban_hanh is None:
                dto.id_co_quan_ban_hanh = []
            else:
                dto.id_co_quan_ban_hanh = json.loads(dto.id_co_quan_ban_hanh)
                

            self.document_validator.validate_document_dtos(dto=dto)

            return self.document_normalizer.normalize_document_dto(dto=dto)
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch DocumentDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "document_id": document_id
                }
            ) from e

    def fetch_big_part_dtos(self, cursor: MySQLCursorAbstract, document_id: int) -> list[BigPartDto]:
        try:
            cursor.execute(
                operation="""
                    SELECT
                        id,
                        vbpl_id,
                        big_part_number,
                        big_part_name
                    FROM vbpl_big_part
                    WHERE vbpl_id = %(document_id)s
                """,
                params={
                    "document_id": document_id
                }
            )

            records = cursor.fetchall()
            dtos = []

            for record in records:
                dtos.append(
                    BigPartDto(
                        id=record.get("id"),
                        vbpl_id=record.get("vbpl_id"),
                        big_part_number=record.get("big_part_number"),
                        big_part_name=record.get("big_part_name")
                    )
                )
            
            for dto in dtos:
                self.document_validator.validate_big_part_dto(dto=dto)
            
            normalized_dtos = []

            for dto in dtos:
                normalized_dtos.append(
                    self.document_normalizer.normalize_big_part_dto(dto=dto)
                )
            
            return normalized_dtos
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch BigPartDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "document_id": document_id
                }
            ) from e
    
    def fetch_chapter_dtos(self, cursor: MySQLCursorAbstract, document_id: int) -> list[ChapterDto]:
        try:
            cursor.execute(
                operation="""
                    SELECT
                        id,
                        vbpl_id,
                        vbpl_big_part_id,
                        chapter_number,
                        chapter_name
                    FROM vbpl_chapter
                    WHERE vbpl_id = %(document_id)s
                """,
                params={
                    "document_id": document_id
                }
            )

            records = cursor.fetchall()
            dtos = []

            for record in records:
                dtos.append(
                    ChapterDto(
                        id=record.get("id"),
                        vbpl_id=record.get("vbpl_id"),
                        vbpl_big_part_id=record.get("vbpl_big_part_id"),
                        chapter_number=record.get("chapter_number"),
                        chapter_name=record.get("chapter_name")
                    )
                )

            for dto in dtos:
                self.document_validator.validate_chapter_dto(dto=dto)

            normalized_dtos = []

            for dto in dtos:
                normalized_dtos.append(
                    self.document_normalizer.normalize_chapter_dto(dto=dto)
                )
            
            return normalized_dtos
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch ChapterDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "document_id": document_id
                }
            ) from e
    
    def fetch_part_dtos(self, cursor: MySQLCursorAbstract, document_id: int) -> list[PartDto]:
        try:
            cursor.execute(
                operation="""
                    SELECT
                        id,
                        vbpl_id,
                        vbpl_chapter_id,
                        part_number,
                        part_name
                    FROM vbpl_part
                    WHERE vbpl_id = %(document_id)s
                """,
                params={
                    "document_id": document_id
                }
            )

            records = cursor.fetchall()
            dtos = []

            for record in records:
                dtos.append(
                    PartDto(
                        id=record.get("id"),
                        vbpl_id=record.get("vbpl_id"),
                        vbpl_chapter_id=record.get("vbpl_chapter_id"),
                        part_number=record.get("part_number"),
                        part_name=record.get("part_name")
                    )
                )

            for dto in dtos:
                self.document_validator.validate_part_dto(dto=dto)
            
            normalized_dtos = []

            for dto in dtos:
                normalized_dtos.append(
                    self.document_normalizer.normalize_part_dto(dto=dto)
                )
            
            return normalized_dtos
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch PartDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "document_id": document_id
                }
            ) from e
    
    def fetch_mini_part_dtos(self, cursor: MySQLCursorAbstract, document_id: int) -> list[MiniPartDto]:
        try:
            cursor.execute(
                operation="""
                    SELECT
                        id,
                        vbpl_id,
                        vbpl_part_id,
                        mini_part_number,
                        mini_part_name
                    FROM vbpl_mini_part
                    WHERE vbpl_id = %(document_id)s
                """,
                params={
                    "document_id": document_id
                }
            )

            records = cursor.fetchall()
            dtos = []

            for record in records:
                dtos.append(
                    MiniPartDto(
                        id=record.get("id"),
                        vbpl_id=record.get("vbpl_id"),
                        vbpl_part_id=record.get("vbpl_part_id"),
                        mini_part_number=record.get("mini_part_number"),
                        mini_part_name=record.get("mini_part_name")
                    )
                )

            for dto in dtos:
                self.document_validator.validate_mini_part_dtos(dto=dto)
            
            normalized_dtos = []

            for dto in dtos:
                normalized_dtos.append(
                    self.document_normalizer.normalize_mini_part_dto(dto=dto)
                )
            
            return normalized_dtos
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch MiniPartDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "document_id": document_id
                }
            ) from e
    
    def fetch_article_dtos(self, cursor: MySQLCursorAbstract, document_id: int) -> list[ArticleDto]:
        try:
            cursor.execute(
                operation="""
                    SELECT
                        id,
                        vbpl_id,
                        vbpl_big_part_id,
                        vbpl_chapter_id,
                        vbpl_part_id,
                        vbpl_mini_part_id,
                        section_number,
                        section_name,
                        section_content,
                        so_phu_luc,
                        effective_date
                    FROM vbpl_section
                    WHERE vbpl_id = %(document_id)s
                """,
                params={
                    "document_id": document_id
                }
            )

            records = cursor.fetchall()
            dtos = []

            for record in records:
                dtos.append(
                    ArticleDto(
                        id=record.get("id"),
                        vbpl_id=record.get("vbpl_id"),
                        vbpl_big_part_id=record.get("vbpl_big_part_id"),
                        vbpl_chapter_id=record.get("vbpl_chapter_id"),
                        vbpl_part_id=record.get("vbpl_part_id"),
                        vbpl_mini_part_id=record.get("vbpl_mini_part_id"),
                        section_number=record.get("section_number"),
                        section_name=record.get("section_name"),
                        section_content=record.get("section_content"),
                        so_phu_luc=record.get("so_phu_luc"),
                        effective_date=record.get("effective_date")
                    )
                )

            for dto in dtos:
                self.document_validator.validate_article_dto(dto=dto)
            
            normalized_dtos = []

            for dto in dtos:
                normalized_dtos.append(
                    self.document_normalizer.normalize_article_dto(dto=dto)
                )
            
            return normalized_dtos
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch ArticleDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "document_id": document_id
                }
            ) from e
    
    def fetch_article_version_dtos(self, cursor: MySQLCursorAbstract, document_id: int) -> list[ArticleVersionDto]:
        try:
            cursor.execute(
                operation="""
                    WITH article_versions AS (
                    SELECT
                        core_noidungsuadoi.id AS version_id,
                        core_noidungsuadoi.vbplsd_id,
                        core_reviewdieuluat.vbpldsd_id,
                        core_noidungsuadoi.dieu AS dieu_sd,
                        core_reviewdieuluat.dieu AS dieu_dsd,
                        core_noidungsuadoi.phu_luc AS phu_luc_sd,
                        core_reviewdieuluat.phu_luc AS phu_luc_dsd,
                        core_reviewdieuluat.loai_vb,
                        core_noidungsuadoi.bai_bo_noi_dung_truoc,
                        core_noidungsuadoi.noi_dung_sua_doi,
                        core_noidungsuadoi.from_date,
                        core_noidungsuadoi.to_date
                    FROM core_reviewdieuluat
                    JOIN core_noidungsuadoi 
                    ON core_reviewdieuluat.id = core_noidungsuadoi.review_dieu_luat_id
                    WHERE
                        core_reviewdieuluat.vbpldsd_id = %(document_id)s AND
                        core_reviewdieuluat.dieu IS NOT NULL AND
                        core_reviewdieuluat.dieu <> ''

                    UNION ALL

                    SELECT
                        core_noidungsuadoi.id AS version_id,
                        core_noidungsuadoi.vbplsd_id,
                        core_reviewdieuluat.vbpldsd_id,
                        core_noidungsuadoi.dieu AS dieu_sd,
                        core_reviewdieuluat.dieu AS dieu_dsd,
                        core_noidungsuadoi.phu_luc AS phu_luc_sd,
                        core_reviewdieuluat.phu_luc AS phu_luc_dsd,
                        core_reviewdieuluat.loai_vb,
                        core_noidungsuadoi.bai_bo_noi_dung_truoc,
                        core_noidungsuadoi.noi_dung_sua_doi,
                        core_noidungsuadoi.from_date,
                        core_noidungsuadoi.to_date
                    FROM core_reviewdieuluat
                    JOIN core_noidungsuadoi 
                    ON core_reviewdieuluat.id = core_noidungsuadoi.review_dieu_luat_id
                    WHERE
                        core_noidungsuadoi.vbplsd_id = %(document_id)s AND
                        core_noidungsuadoi.dieu IS NOT NULL AND
                        core_noidungsuadoi.dieu <> ''
                )
                SELECT
                    article_versions.version_id,
                    article_versions.vbplsd_id,
                    article_versions.vbpldsd_id,
                    article_versions.dieu_sd,
                    article_versions.dieu_dsd,
                    vs1.id AS dieu_sd_id,
                    vs2.id AS dieu_dsd_id,
                    article_versions.phu_luc_sd,
                    article_versions.phu_luc_dsd,
                    article_versions.loai_vb,
                    article_versions.from_date,
                    article_versions.to_date,
                    article_versions.bai_bo_noi_dung_truoc,
                    article_versions.noi_dung_sua_doi
                FROM article_versions
                JOIN vbpl_section AS vs1
                ON
                    article_versions.vbplsd_id = vs1.vbpl_id AND
                    article_versions.dieu_sd COLLATE utf8mb4_general_ci
                        = vs1.section_number COLLATE utf8mb4_general_ci AND
                    NULLIF(article_versions.phu_luc_sd, '') COLLATE utf8mb4_general_ci 
                        <=> NULLIF(vs1.so_phu_luc, '') COLLATE utf8mb4_general_ci
                JOIN vbpl_section AS vs2
                ON
                    article_versions.vbpldsd_id = vs2.vbpl_id AND
                    article_versions.dieu_dsd COLLATE utf8mb4_general_ci 
                        = vs2.section_number COLLATE utf8mb4_general_ci AND
                    NULLIF(article_versions.phu_luc_dsd, '') COLLATE utf8mb4_general_ci 
                        <=> NULLIF(vs2.so_phu_luc, '') COLLATE utf8mb4_general_ci
                """,
                params={
                    "document_id": document_id
                }
            )

            records = cursor.fetchall()
            dtos = []

            for record in records:
                dtos.append(
                    ArticleVersionDto(
                        version_id=record.get("version_id"),
                        vbplsd_id=record.get("vbplsd_id"),
                        vbpldsd_id=record.get("vbpldsd_id"),
                        dieu_sd_id=record.get("dieu_sd_id"),
                        dieu_dsd_id=record.get("dieu_dsd_id"),
                        phu_luc_sd=record.get("phu_luc_sd"),
                        phu_luc_dsd=record.get("phu_luc_dsd"),
                        loai_vb=record.get("loai_vb"),
                        from_date=record.get("from_date"),
                        to_date=record.get("to_date"),
                        bai_bo_noi_dung_truoc=record.get("bai_bo_noi_dung_truoc"),
                        noi_dung_sua_doi=record.get("noi_dung_sua_doi")
                    )
                )

            for dto in dtos:
                self.document_validator.validate_chapter_dto(dto=dto)
            
            normalized_dtos = []

            for dto in dtos:
                normalized_dtos.append(
                    self.document_normalizer.normalize_article_version_dto(dto=dto)
                )
            
            return normalized_dtos
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch ArticleVersionDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "document_id": document_id
                }
            ) from e
    
    def fetch_document_mapping_dtos(self, cursor: MySQLCursorAbstract, document_id: int) -> list[DocumentMappingDto]:
        try:
            cursor.execute(
                operation="""
                    SELECT
                        id,
                        from_document_id,
                        to_document_id,
                        relationship_type
                    FROM vbpl_doc_map
                    WHERE
                        from_document_id = %(document_id)s OR
                        to_document_id = %(document_id)s
                """,
                params={
                    "document_id": document_id
                }
            )

            records = cursor.fetchall()
            dtos = []

            for record in records:
                dtos.append(
                    DocumentMappingDto(
                        id=record.get("id"),
                        from_document_id=record.get("from_document_id"),
                        to_document_id=record.get("to_document_id"),
                        relationship_type=record.get("relationship_type")
                    )
                )

            for dto in dtos:
                self.document_validator.validate_document_mapping_dto(dto=dto)
            
            normalized_dtos = []

            for dto in dtos:
                normalized_dtos.append(
                    self.document_normalizer.normalize_document_mapping_dto(dto=dto)
                )
            
            return normalized_dtos
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch DocumentMappingDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "document_id": document_id
                }
            ) from e
    
    def fetch_document_type_dto(self, cursor: MySQLCursorAbstract, document_type_id: int) -> DocumentTypeDto:
        try:
            cursor.execute(
                operation="""
                    SELECT id, loai_van_ban
                    FROM vbpl_doc_type
                    WHERE id = %(document_type_id)s
                """,
                params={
                    "document_type_id": document_type_id
                }
            )

            record = cursor.fetchone()

            dto = DocumentTypeDto(
                id=record.get("id"),
                loai_van_ban=record.get("loai_van_ban")
            )

            self.document_validator.validate_document_type_dto(dto=dto)

            return self.document_normalizer.normalize_document_type_dto(dto=dto)
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch DocumentTypeDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "document_type_id": document_type_id
                }
            ) from e
    
    def fetch_issuing_authority_dtos(self, cursor: MySQLCursorAbstract, issuing_authority_ids: list[int]) -> list[IssuingAuthorityDto]:
        try:
            placeholders = ",".join(["%s"] * len(issuing_authority_ids))

            query = f"""
                SELECT
                    id,
                    co_quan_ban_hanh
                FROM vbpl_issuing_authority
                WHERE id IN ({placeholders})
            """

            cursor.execute(query, issuing_authority_ids)
            records = cursor.fetchall()
            dtos = []

            for record in records:
                dtos.append(
                    IssuingAuthorityDto(
                        id=record.get("id"),
                        co_quan_ban_hanh=record.get("co_quan_ban_hanh")
                    )
                )

            self.document_validator.validate_issuing_authority_dtos(dtos=dtos)

            return self.document_normalizer.normalize_issuing_authority_dtos(dtos=dtos)
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch IssuingAuthorityDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "issuing_authority_ids": issuing_authority_ids
                }
            ) from e
    
    def fetch_sector_dto(self, cursor: MySQLCursorAbstract, sector_id: int) -> SectorDto:
        try:
            cursor.execute(
                operation="""
                    SELECT id, linh_vuc
                    FROM vbpl_sector
                    WHERE id = %(sector_id)s
                """,
                params={
                    "sector_id": sector_id
                }
            )

            record = cursor.fetchone()

            dto = SectorDto(
                id=record.get("id"),
                linh_vuc=record.get("linh_vuc")
            )

            self.document_validator.validate_sector_dto(dto=dto)

            return self.document_normalizer.normalize_sector_dto(dto=dto)
        except Exception as e:
            raise FetchDataError(
                message="Failed to fetch SectorDto",
                context={
                    "host": self.mysql_client.config.host,
                    "database": self.mysql_client.config.database,
                    "type": "document",
                    "sector_id": sector_id
                }
            ) from e
    
    def fetch_all(self, document_id: int) -> FetchDocumentResult:
        connection, cursor = self.mysql_client.get_connection()
        
        try:
            document_dto = self.fetch_document_dto(cursor=cursor, document_id=document_id)
            big_part_dtos = self.fetch_big_part_dtos(cursor=cursor, document_id=document_id)
            chapter_dtos = self.fetch_chapter_dtos(cursor=cursor, document_id=document_id)
            part_dtos = self.fetch_part_dtos(cursor=cursor, document_id=document_id)
            mini_part_dtos = self.fetch_mini_part_dtos(cursor=cursor, document_id=document_id)
            article_dtos = self.fetch_article_dtos(cursor=cursor, document_id=document_id)
            article_version_dtos = self.fetch_article_version_dtos(cursor=cursor, document_id=document_id)
            document_mapping_dtos = self.fetch_document_mapping_dtos(cursor=cursor, document_id=document_id)
            
            document_type_dto = self.fetch_document_type_dto(
                cursor=cursor,
                document_type_id=document_dto.id_loai_van_ban
            )

            issuing_authority_dtos = self.fetch_issuing_authority_dtos(
                cursor=cursor,
                issuing_authority_ids=document_dto.id_co_quan_ban_hanh
            )

            sector_dto = self.fetch_sector_dto(
                cursor=cursor,
                sector_id=document_dto.id_linh_vuc
            )

            return FetchDocumentResult(
                document_dto=document_dto,
                big_part_dtos=big_part_dtos,
                chapter_dtos=chapter_dtos,
                part_dtos=part_dtos,
                mini_part_dtos=mini_part_dtos,
                article_dtos=article_dtos,
                article_version_dtos=article_version_dtos,
                document_mapping_dtos=document_mapping_dtos,
                document_type_dto=document_type_dto,
                issuing_authority_dtos=issuing_authority_dtos,
                sector_dto=sector_dto
            )
        except Exception as e:
            raise FetchDataError(message="Failed to fetch document data") from e
        finally:
            cursor.close()
            connection.close()
