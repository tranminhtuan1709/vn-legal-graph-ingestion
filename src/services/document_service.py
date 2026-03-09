import uuid
import time

from repositories.document_repository import DocumentRepository
from repositories.graph_repository import GraphRepository
from interface.dtos.internal.graph.triple import Triple

from interface.dtos.internal.graph.nodes.document_node import DocumentNode
from interface.dtos.internal.graph.nodes.big_part_node import BigPartNode
from interface.dtos.internal.graph.nodes.chapter_node import ChapterNode
from interface.dtos.internal.graph.nodes.part_node import PartNode
from interface.dtos.internal.graph.nodes.mini_part_node import MiniPartNode
from interface.dtos.internal.graph.nodes.article_node import ArticleNode
from interface.dtos.internal.graph.nodes.document_type_node import DocumentTypeNode
from interface.dtos.internal.graph.nodes.issuing_authority_node import IssuingAuthorityNode
from interface.dtos.internal.graph.nodes.sector_node import SectorNode

from interface.dtos.internal.graph.edges.amend_edge import AmendEdge
from interface.dtos.internal.graph.edges.concern_edge import ConcernEdge
from interface.dtos.internal.graph.edges.consolidate_edge import ConsolidateEdge
from interface.dtos.internal.graph.edges.contain_edge import ContainEdge
from interface.dtos.internal.graph.edges.correct_edge import CorrectEdge
from interface.dtos.internal.graph.edges.guide_edge import GuideEdge
from interface.dtos.internal.graph.edges.implement_amendment_edge import ImplementAmendmentEdge
from interface.dtos.internal.graph.edges.is_amended_to_edge import IsAmendedToEdge
from interface.dtos.internal.graph.edges.is_edge import IsEdge
from interface.dtos.internal.graph.edges.issue_edge import IssueEdge
from interface.dtos.internal.graph.edges.replace_edge import ReplaceEdge
from interface.dtos.internal.graph.edges.supplement_edge import SupplementEdge
from interface.dtos.internal.graph.edges.suspend_edge import SuspendEdge

from utils.datetime_utils import get_current_timestamp
from utils.logger import logger


class DocumentService:
    def __init__(
        self,
        document_repository: DocumentRepository,
        graph_repository: GraphRepository,
        uuid_namespace: str
    ) -> None:
        self.document_repository = document_repository
        self.graph_repository = graph_repository
        self.uuid_namespace = uuid_namespace
    
    def ingest_document(self, document_id: int) -> None:
        start_time = time.time()
        
        try:
            document_data = self.document_repository.fetch_all(document_id=document_id)

            nodes = []
            triples = []

            nodes.append(
                DocumentNode(
                    node_id=uuid.uuid5(self.uuid_namespace, f"Document_{document_data.document_dto.id}"),
                    node_label="Document",
                    created_at=get_current_timestamp(),
                    source="legal_document",
                    document_id=document_data.document_dto.id,
                    document_number=document_data.document_dto.so_ky_hieu,
                    document_name=document_data.document_dto.ten_hien_thi,
                    issued_date=document_data.document_dto.ngay_ban_hanh,
                    effective_date=document_data.document_dto.ngay_co_hieu_luc,
                    expiry_date=document_data.document_dto.ngay_het_han,
                    status=document_data.document_dto.trang_thai,
                    summary=document_data.document_dto.chu_thich_nho
                )
            )

            for dto in document_data.big_part_dtos:
                nodes.append(
                    BigPartNode(
                        node_id=uuid.uuid5(self.uuid_namespace, f"BigPart_{dto.id}"),
                        node_label="BigPart",
                        created_at=get_current_timestamp(),
                        source="legal_document",
                        big_part_id=dto.id,
                        big_part_number=dto.big_part_number,
                        big_part_name=dto.big_part_name
                    )
                )

                triples.append(
                    Triple(
                        from_node_id=uuid.uuid5(self.uuid_namespace, f"Document_{dto.vbpl_id}"),
                        to_node_id=uuid.uuid5(self.uuid_namespace, f"BigPart_{dto.id}"),
                        edge=ContainEdge(
                            edge_type="CONTAIN",
                            created_at=get_current_timestamp
                        )
                    )
                )
            
            for dto in document_data.chapter_dtos:
                nodes.append(
                    ChapterNode(
                        node_id=uuid.uuid5(self.uuid_namespace, f"Chapter_{dto.id}"),
                        node_label="Chapter",
                        created_at=get_current_timestamp(),
                        source="legal_document",
                        chapter_id=dto.id,
                        chapter_number=dto.chapter_number,
                        chapter_name=dto.chapter_name
                    )
                )

                if dto.vbpl_big_part_id is not None:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"BigPart_{dto.vbpl_big_part_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Chapter_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp
                            )
                        )
                    )
                else:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Document_{dto.vbpl_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Chapter_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp
                            )
                        )
                    )

            for dto in document_data.part_dtos:
                nodes.append(
                    PartNode(
                        node_id=uuid.uuid5(self.uuid_namespace, f"Part_{dto.id}"),
                        node_label="Part",
                        created_at=get_current_timestamp(),
                        source="legal_document",
                        part_id=dto.id,
                        part_number=dto.part_number,
                        part_name=dto.part_name
                    )
                )

                if dto.vbpl_chapter_id is not None:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Chapter_{dto.vbpl_chapter_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Part_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp()
                            )
                        )
                    )
                else:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Document_{dto.vbpl_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Part_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp()
                            )
                        )
                    )

            for dto in document_data.mini_part_dtos:
                nodes.append(
                    MiniPartNode(
                        node_id=uuid.uuid5(self.uuid_namespace, f"MiniPart_{dto.id}"),
                        node_label="MiniPart",
                        created_at=get_current_timestamp(),
                        source="legal_document",
                        mini_part_id=dto.id,
                        mini_part_number=dto.mini_part_number,
                        mini_part_name=dto.mini_part_name
                    )
                )

                if dto.vbpl_part_id is not None:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Part_{dto.vbpl_part_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"MiniPart_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp()
                            )
                        )
                    )
                else:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Document_{dto.vbpl_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"MiniPart_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp()
                            )
                        )
                    )
            
            for dto in document_data.article_dtos:
                nodes.append(
                    ArticleNode(
                        node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.id}"),
                        node_label="Article",
                        created_at=get_current_timestamp,
                        source="legal_document",
                        article_id=dto.id,
                        article_number=dto.section_number,
                        article_name=dto.section_name,
                        article_content=dto.section_content,
                        effective_date=dto.effective_date,
                        appendix=dto.so_phu_luc
                    )
                )

                if dto.vbpl_mini_part_id is not None:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"MiniPart_{dto.vbpl_mini_part_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp
                            )
                        )
                    )
                elif dto.vbpl_part_id is not None:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Part_{dto.vbpl_part_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp
                            )
                        )
                    )
                elif dto.vbpl_chapter_id is not None:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Chapter_{dto.vbpl_chapter_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp
                            )
                        )
                    )
                elif dto.vbpl_big_part_id is not None:
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"BigPart_{dto.vbpl_big_part_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.id}"),
                            edge=ContainEdge(
                                edge_type="CONTAIN",
                                created_at=get_current_timestamp
                            )
                        )
                    )

            for dto in document_data.issuing_authority_dtos:
                nodes.append(
                    IssuingAuthorityNode(
                        node_id=uuid.uuid5(self.uuid_namespace, f"IssuingAuthority_{dto.id}"),
                        node_label="IssuingAuthority",
                        created_at=get_current_timestamp,
                        source="legal_document",
                        issuing_authority_id=dto.id,
                        issuing_authority_name=dto.co_quan_ban_hanh
                    )
                )

                triples.append(
                    Triple(
                        from_node_id=uuid.uuid5(self.uuid_namespace, f"IssuingAuthority_{dto.id}"),
                        to_node_id=uuid.uuid5(self.uuid_namespace, f"Document_{document_data.document_dto.id}"),
                        edge=IssueEdge(
                            edge_type="ISSUE",
                            created_at=get_current_timestamp
                        )
                    )
                )
            
            nodes.append(
                DocumentTypeNode(
                    node_id=uuid.uuid5(self.uuid_namespace, f"DocumentType_{document_data.document_type_dto.id}"),
                    node_label="DocumentType",
                    created_at=get_current_timestamp,
                    source="legal_document",
                    document_type_id=document_data.document_type_dto.id,
                    document_type_name=document_data.document_type_dto.loai_van_ban
                )
            )

            triples.append(
                Triple(
                    from_node_id=uuid.uuid5(self.uuid_namespace, f"Document_{document_data.document_dto.id}"),
                    to_node_id=uuid.uuid5(self.uuid_namespace, f"DocumentType_{document_data.document_type_dto.id}"),
                    edge=IsEdge(
                        edge_type="IS",
                        created_at=get_current_timestamp
                    )
                )
            )

            nodes.append(
                SectorNode(
                    node_id=uuid.uuid5(self.uuid_namespace, f"Sector_{document_data.sector_dto.id}"),
                    node_label="Sector",
                    created_at=get_current_timestamp,
                    source="legal_document",
                    sector_id=document_data.sector_dto.id,
                    sector_name=document_data.sector_dto.linh_vuc
                )
            )

            triples.append(
                Triple(
                    from_node_id=uuid.uuid5(self.uuid_namespace, f"Document_{document_data.document_dto.id}"),
                    to_node_id=uuid.uuid5(self.uuid_namespace, f"Sector_{document_data.sector_dto.id}"),
                    edge=ConcernEdge(
                        edge_type="CONCERN",
                        created_at=get_current_timestamp
                    )
                )
            )
        
            edge_mapping = {
                "huong_dan": (GuideEdge, "GUIDE"),
                "thay_the": (ReplaceEdge, "REPLACE"),
                "sua_doi": (AmendEdge, "AMEND"),
                "dinh_chinh": (CorrectEdge, "CORRECT"),
                "hop_nhat": (ConsolidateEdge, "CONSOLIDATE"),
            }

            for dto in document_data.document_mapping_dtos:
                edge_class, edge_type = edge_mapping[dto.relationship_type]

                triples.append(
                    Triple(
                        from_node_id=uuid.uuid5(self.uuid_namespace, f"Document_{dto.from_document_id}"),
                        to_node_id=uuid.uuid5(self.uuid_namespace, f"Document_{dto.to_document_id}"),
                        edge=edge_class(
                            edge_type=edge_type,
                            created_at=get_current_timestamp,
                            document_mapping_id=dto.id
                        )
                    )
                )
            
            for dto in document_data.article_version_dtos:
                if dto.loai_vb == "SĐ":
                    nodes.append(
                        ArticleNode(
                            node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.version_id}"),
                            node_label="Article",
                            created_at=get_current_timestamp,
                            source="legal_document",
                            article_id=dto.version_id,
                            article_number=dto.dieu_dsd,
                            article_content=dto.noi_dung_sua_doi,
                            effective_date=dto.from_date,
                            appendix=dto.phu_luc_dsd
                        )
                    )

                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.dieu_dsd_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.version_id}"),
                            edge=IsAmendedToEdge(
                                edge_type="IS_AMENDED_TO",
                                created_at=get_current_timestamp
                            )
                        )
                    )

                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.dieu_sd_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.version_id}"),
                            edge=ImplementAmendmentEdge(
                                edge_type="IMPLEMENT_AMENDMENT",
                                created_at=get_current_timestamp,
                                version_id=dto.version_id,
                                from_date=dto.from_date,
                                to_date=dto.to_date,
                                abolish_previous_content=dto.bai_bo_noi_dung_truoc
                            )
                        )
                    )
                elif dto.loai_vb == "BS":
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.dieu_sd_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.dieu_dsd_id}"),
                            edge=SupplementEdge(
                                edge_type="SUPPLEMENT",
                                created_at=get_current_timestamp,
                                version_id=dto.version_id,
                                from_date=dto.from_date,
                                to_date=dto.to_date
                            )
                        )
                    )
                elif dto.loai_vb == "NHL":
                    triples.append(
                        Triple(
                            from_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.dieu_sd_id}"),
                            to_node_id=uuid.uuid5(self.uuid_namespace, f"Article_{dto.dieu_dsd_id}"),
                            edge=SuspendEdge(
                                edge_type="SUPPLEMENT",
                                created_at=get_current_timestamp,
                                version_id=dto.version_id,
                                from_date=dto.from_date,
                                to_date=dto.to_date
                            )
                        )
                    )
            
            self.graph_repository.detach_document_subgraph(
                node_id=uuid.uuid5(self.uuid_namespace, f"Document_{document_id}")
            )

            self.graph_repository.create_nodes(nodes=nodes)
            self.graph_repository.create_edges(triples=triples)
        except Exception:
            raise
        finally:
            logger.info(msg=f"{round(time.time() - start_time, 4)} s")
