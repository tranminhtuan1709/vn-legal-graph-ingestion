import time

from dtos.document.document_data import DocumentData

from dtos.graph.nodes.node import Node
from dtos.graph.nodes.document_node import DocumentNode
from dtos.graph.nodes.big_part_node import BigPartNode
from dtos.graph.nodes.chapter_node import ChapterNode
from dtos.graph.nodes.part_node import PartNode
from dtos.graph.nodes.mini_part_node import MiniPartNode
from dtos.graph.nodes.article_node import ArticleNode
from dtos.graph.nodes.issuing_authority_node import IssuingAuthorityNode
from dtos.graph.nodes.document_type_node import DocumentTypeNode
from dtos.graph.nodes.sector_node import SectorNode

from dtos.graph.edges.edge import Edge
from dtos.graph.edges.guide_edge import GuideEdge
from dtos.graph.edges.amend_edge import AmendEdge
from dtos.graph.edges.replace_edge import ReplaceEdge
from dtos.graph.edges.correct_edge import CorrectEdge
from dtos.graph.edges.consolidate_edge import ConsolidateEdge
from dtos.graph.edges.contain_edge import ContainEdge
from dtos.graph.edges.is_edge import IsEdge
from dtos.graph.edges.concern_edge import ConcernEdge
from dtos.graph.edges.supplement_edge import SupplementEdge
from dtos.graph.edges.suspend_edge import SuspendEdge
from dtos.graph.edges.is_amended_to_edge import IsAmendedToEdge
from dtos.graph.edges.implement_amendment_edge import ImplementAmendmentEdge

from utils.logger import logger
from utils.uuid_utils import get_node_id
from utils.datetime_utils import get_current_timestamp


def document_to_graph(document_data: DocumentData) -> tuple[list[Node], list[Edge]]:
    start_time = time.time()

    try:
        nodes = []
        edges = []

        nodes.append(
            DocumentNode(
                node_id=get_node_id(business_id=document_data.document_dto.id, node_label="Document"),
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
                small_node=document_data.document_dto.chu_thich_nho
            )
        )

        for dto in document_data.big_part_dtos:
            nodes.append(
                BigPartNode(
                    node_id=get_node_id(business_id=dto.id, node_label="BigPart"),
                    node_label="BigPart",
                    created_at=get_current_timestamp(),
                    source="legal_document",
                    big_part_id=dto.id,
                    big_part_number=dto.big_part_number,
                    big_part_name=dto.big_part_name
                )
            )

            edges.append(
                ContainEdge(
                    from_node_id=get_node_id(business_id=document_data.document_dto.id, node_label="Document"),
                    to_node_id=get_node_id(business_id=dto.id, node_label="BigPart"),
                    edge_type="CONTAIN",
                    created_at=get_current_timestamp()
                )
            )

        for dto in document_data.chapter_dtos:
            nodes.append(
                ChapterNode(
                    node_id=get_node_id(business_id=dto.id, node_label="Chapter"),
                    node_label="Chapter",
                    created_at=get_current_timestamp(),
                    source="legal_document",
                    chapter_id=dto.id,
                    chapter_number=dto.chapter_number,
                    chapter_name=dto.chapter_name
                )
            )

            if dto.vbpl_big_part_id is not None:
                from_node_id = get_node_id(business_id=dto.vbpl_big_part_id, node_label="BigPart")
            else:
                from_node_id = get_node_id(business_id=dto.vbpl_id, node_label="Document")

            edges.append(
                ContainEdge(
                    from_node_id=from_node_id,
                    to_node_id=get_node_id(business_id=dto.id, node_label="Chapter"),
                    edge_type="CONTAIN",
                    created_at=get_current_timestamp()
                )
            )
        
        for dto in document_data.part_dtos:
            nodes.append(
                PartNode(
                    node_id=get_node_id(business_id=dto.id, node_label="Part"),
                    node_label="Part",
                    created_at=get_current_timestamp(),
                    source="legal_document",
                    part_id=dto.id,
                    part_number=dto.part_number,
                    part_name=dto.part_name
                )
            )

            if dto.vbpl_chapter_id is not None:
                from_node_id = get_node_id(business_id=dto.vbpl_chapter_id, node_label="Chapter")
            else:
                from_node_id = get_node_id(business_id=dto.vbpl_id, node_label="Document")

            edges.append(
                ContainEdge(
                    from_node_id=from_node_id,
                    to_node_id=get_node_id(business_id=dto.id, node_label="Part"),
                    edge_type="CONTAIN",
                    created_at=get_current_timestamp()
                )
            )
        
        for dto in document_data.mini_part_dtos:
            nodes.append(
                MiniPartNode(
                    node_id=get_node_id(business_id=dto.id, node_label="MiniPart"),
                    node_label="MiniPart",
                    created_at=get_current_timestamp(),
                    source="legal_document",
                    mini_part_id=dto.id,
                    mini_part_number=dto.mini_part_number,
                    mini_part_name=dto.mini_part_name
                )
            )

            if dto.vbpl_part_id is not None:
                from_node_id = get_node_id(business_id=dto.vbpl_part_id, node_label="Part")
            else:
                from_node_id = get_node_id(business_id=dto.vbpl_id, node_label="Document")

            edges.append(
                ContainEdge(
                    from_node_id=from_node_id,
                    to_node_id=get_node_id(business_id=dto.id, node_label="MiniPart"),
                    edge_type="CONTAIN",
                    created_at=get_current_timestamp()
                )
            )
        
        for dto in document_data.article_dtos:
            nodes.append(
                ArticleNode(
                    node_id=get_node_id(business_id=dto.id, node_label="Article"),
                    node_label="Article",
                    created_at=get_current_timestamp(),
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
                from_node_id = get_node_id(business_id=dto.vbpl_mini_part_id, node_label="MiniPart")
            elif dto.vbpl_part_id is not None:
                from_node_id = get_node_id(business_id=dto.vbpl_part_id, node_label="Part")
            elif dto.vbpl_chapter_id is not None:
                from_node_id = get_node_id(business_id=dto.vbpl_chapter_id, node_label="Chapter")
            elif dto.vbpl_big_part_id is not None:
                from_node_id = get_node_id(business_id=dto.vbpl_big_part_id, node_label="BigPart")
            else:
                from_node_id = get_node_id(business_id=dto.vbpl_id, node_label="Document")
            
            edges.append(
                ContainEdge(
                    from_node_id=from_node_id,
                    to_node_id=get_node_id(business_id=dto.id, node_label="Article"),
                    edge_type="CONTAIN",
                    created_at=get_current_timestamp()
                )
            )
        
        for dto in document_data.article_version_dtos:
            if dto.loai_vb == "SĐ":
                nodes.append(
                    ArticleNode(
                        node_id=get_node_id(business_id=dto.version_id, node_label="Article"),
                        node_label="Article",
                        created_at=get_current_timestamp(),
                        source="legal_document",
                        article_id=dto.version_id,
                        article_number=dto.dieu_dsd,
                        article_name=None,
                        article_content=dto.noi_dung_sua_doi,
                        effective_date=dto.from_date,
                        appendix=dto.phu_luc_dsd
                    )
                )

                edges.append(
                    IsAmendedToEdge(
                        from_node_id=get_node_id(business_id=dto.dieu_sd_id, node_label="Article"),
                        to_node_id=get_node_id(business_id=dto.dieu_dsd_id, node_label="Article"),
                        edge_type="IS_AMENDED_TO",
                        created_at=get_current_timestamp()
                    )
                )
            elif dto.loai_vb == "BS":
                edges.append(
                    SupplementEdge(
                        from_node_id=get_node_id(business_id=dto.dieu_sd_id, node_label="Article"),
                        to_node_id=get_node_id(business_id=dto.dieu_dsd_id, node_label="Article"),
                        edge_type="SUPPLEMENT",
                        created_at=get_current_timestamp(),
                        from_date=dto.from_date,
                        to_date=dto.to_date
                    )
                )
            elif dto.loai_vb == "NHL":
                edges.append(
                    SuspendEdge(
                        from_node_id=get_node_id(business_id=dto.dieu_sd_id, node_label="Article"),
                        to_node_id=get_node_id(business_id=dto.dieu_dsd_id, node_label="Article"),
                        edge_type="SUSPEND",
                        created_at=get_current_timestamp(),
                        from_date=dto.from_date,
                        to_date=dto.to_date
                    )
                )

        for dto in document_data.document_mapping_dtos:
            from_node_id = get_node_id(business_id=dto.from_document_id, node_label="Document")
            to_node_id = get_node_id(business_id=dto.to_document_id, node_label="Document")
            
            if dto.relationship_type == "huong_dan":
                edges.append(
                    GuideEdge(
                        from_node_id=from_node_id,
                        to_node_id=to_node_id,
                        edge_type="GUIDE",
                        created_at=get_current_timestamp(),
                        document_mapping_id=dto.id
                    )
                )
            elif dto.relationship_type == "sua_doi":
                edges.append(
                    AmendEdge(
                        from_node_id=from_node_id,
                        to_node_id=to_node_id,
                        edge_type="AMEND",
                        created_at=get_current_timestamp(),
                        document_mapping_id=dto.id
                    )
                )
            elif dto.relationship_type == "thay_the":
                edges.append(
                    ReplaceEdge(
                        from_node_id=from_node_id,
                        to_node_id=to_node_id,
                        edge_type="REPLACE",
                        created_at=get_current_timestamp(),
                        document_mapping_id=dto.id
                    )
                )
            elif dto.relationship_type == "dinh_chinh":
                edges.append(
                    CorrectEdge(
                        from_node_id=from_node_id,
                        to_node_id=to_node_id,
                        edge_type="CORRECT",
                        created_at=get_current_timestamp(),
                        document_mapping_id=dto.id
                    )
                )
            elif dto.relationship_type == "hop_nhat":
                edges.append(
                    ConsolidateEdge(
                        from_node_id=from_node_id,
                        to_node_id=to_node_id,
                        edge_type="CONSOLIDATE",
                        created_at=get_current_timestamp(),
                        document_mapping_id=dto.id
                    )
                )

        return nodes, edges    
    except Exception:
        raise
    finally:
        logger.info(f"{time.time() - start_time} s")
    