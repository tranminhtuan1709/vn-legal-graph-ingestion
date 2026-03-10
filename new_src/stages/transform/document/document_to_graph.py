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
                created_at=get_current_timestamp,
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
                    
                )
            )
    except Exception:
        raise
    finally:
        logger.info(f"{time.time() - start_time} s")
    