from dtos.document.document_data import DocumentData
from dtos.document.document_dto import DocumentDto
from dtos.document.big_part_dto import BigPartDto
from dtos.document.chapter_dto import ChapterDto
from dtos.document.part_dto import PartDto
from dtos.document.mini_part_dto import MiniPartDto
from dtos.document.article_dto import ArticleDto
from dtos.document.article_version_dto import ArticleVersionDto
from dtos.document.document_mapping_dto import DocumentMappingDto

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
from dtos.graph.edges.issue_edge import IssueEdge
from dtos.graph.edges.supplement_edge import SupplementEdge
from dtos.graph.edges.suspend_edge import SuspendEdge
from dtos.graph.edges.is_amended_to_edge import IsAmendedToEdge
from dtos.graph.edges.implement_amendment_edge import ImplementAmendmentEdge

from utils.uuid_utils import get_node_id
from utils.datetime_utils import get_current_timestamp


def document_dto_to_graph(document_dto: DocumentDto) -> tuple[list[Node], list[Edge]]:
    nodes: list[Node] = []
    edges: list[Edge] = []

    if document_dto is None:
        return [], []

    nodes.append(
        DocumentNode(
            node_id=get_node_id(business_id=document_dto.document_id, node_label="Document"),
            node_label="Document",
            created_at=get_current_timestamp(),
            source="legal_document",
            document_id=document_dto.document_id,
            document_number=document_dto.document_number,
            document_name=document_dto.document_name,
            issued_date=document_dto.issued_date,
            effective_date=document_dto.effective_date,
            expiry_date=document_dto.expiry_date,
            status=document_dto.status,
            small_node=document_dto.small_note
        )
    )

    if document_dto.sector_id is not None and document_dto.sector is not None:
        nodes.append(
            SectorNode(
                node_id=get_node_id(business_id=document_dto.sector_id, node_label="Sector"),
                node_label="Sector",
                created_at=get_current_timestamp(),
                source="legal_document",
                sector_id=document_dto.sector_id,
                sector_name=document_dto.sector
            )
        )

        edges.append(
            ConcernEdge(
                from_node_id=get_node_id(business_id=document_dto.document_id, node_label="Document"),
                to_node_id=get_node_id(business_id=document_dto.sector_id, node_label="Sector"),
                edge_type="CONCERN",
                created_at=get_current_timestamp()
            )
        )
    
    if document_dto.document_type_id is not None and document_dto.document_type is not None:
        nodes.append(
            DocumentTypeNode(
                node_id=get_node_id(business_id=document_dto.document_type_id, node_label="DocumentType"),
                node_label="DocumentType",
                created_at=get_current_timestamp(),
                source="legal_document",
                document_type_id=document_dto.document_type_id,
                document_type_name=document_dto.document_type
            )
        )

        edges.append(
            IsEdge(
                from_node_id=get_node_id(business_id=document_dto.document_id, node_label="Document"),
                to_node_id=get_node_id(business_id=document_dto.document_type_id, node_label="DocumentType"),
                edge_type="IS",
                created_at=get_current_timestamp()
            )
        )
    
    if (
        len(document_dto.issuing_authorities) > 0 and
        len(document_dto.issuing_authority_ids) > 0 and
        len(document_dto.issuing_authorities) == len(document_dto.issuing_authority_ids)
    ):
        for i in range(len(document_dto.issuing_authorities)):
            nodes.append(
                IssuingAuthorityNode(
                    node_id=get_node_id(business_id=document_dto.issuing_authorities[i], node_label="IssuingAuthority"),
                    node_label="IssuingAuthority",
                    created_at=get_current_timestamp(),
                    source="legal_document",
                    issuing_authority_id=document_dto.issuing_authority_ids[i],
                    issuing_authority_name=document_dto.issuing_authorities[i]
                )
            )

            edges.append(
                IssueEdge(
                    from_node_id=get_node_id(document_dto.issuing_authority_ids[i], "IssuingAuthority"),
                    to_node_id=get_node_id(document_dto.document_id, node_label="Document"),
                    edge_type="ISSUE",
                    created_at=get_current_timestamp()
                )
            )

    return nodes, edges


def big_part_dtos_to_graph(big_part_dtos: list[BigPartDto]) -> tuple[list[Node], list[Edge]]:
    nodes: list[Node] = []
    edges: list[Edge] = []

    if len(big_part_dtos) == 0:
        return nodes, edges

    for dto in big_part_dtos:
        nodes.append(
            BigPartNode(
                node_id=get_node_id(business_id=dto.big_part_id, node_label="BigPart"),
                node_label="BigPart",
                created_at=get_current_timestamp(),
                source="legal_document",
                big_part_id=dto.big_part_id,
                big_part_number=dto.big_part_number,
                big_part_name=dto.big_part_name
            )
        )

        edges.append(
            ContainEdge(
                from_node_id=get_node_id(business_id=dto.document_id, node_label="Document"),
                to_node_id=get_node_id(business_id=dto.big_part_id, node_label="BigPart"),
                edge_type="CONTAIN",
                created_at=get_current_timestamp()
            )
        )
    
    return nodes, edges


def chapter_dtos_to_graph(chapter_dtos: list[ChapterDto]) -> tuple[list[Node], list[Edge]]:
    nodes: list[Node] = []
    edges: list[Edge] = []

    if len(chapter_dtos) == 0:
        return nodes, edges

    for dto in chapter_dtos:
        nodes.append(
            ChapterNode(
                node_id=get_node_id(business_id=dto.chapter_id, node_label="Chapter"),
                node_label="Chapter",
                created_at=get_current_timestamp(),
                source="legal_document",
                chapter_id=dto.chapter_id,
                chapter_number=dto.chapter_number,
                chapter_name=dto.chapter_name
            )
        )

        if dto.big_part_id is not None:
            from_node_id = get_node_id(business_id=dto.big_part_id, node_label="BigPart")
        else:
            from_node_id = get_node_id(business_id=dto.document_id, node_label="Document")

        edges.append(
            ContainEdge(
                from_node_id=from_node_id,
                to_node_id=get_node_id(business_id=dto.chapter_id, node_label="Chapter"),
                edge_type="CONTAIN",
                created_at=get_current_timestamp()
            )
        )
    
    return nodes, edges


def part_dtos_to_graph(part_dtos: list[PartDto]) -> tuple[list[Node], list[Edge]]:
    nodes: list[Node] = []
    edges: list[Edge] = []

    if len(part_dtos):
        return nodes, edges

    for dto in part_dtos:
        nodes.append(
            PartNode(
                node_id=get_node_id(business_id=dto.part_id, node_label="Part"),
                node_label="Part",
                created_at=get_current_timestamp(),
                source="legal_document",
                part_id=dto.part_id,
                part_number=dto.part_number,
                part_name=dto.part_name
            )
        )

        if dto.chapter_id is not None:
            from_node_id = get_node_id(business_id=dto.chapter_id, node_label="Chapter")
        else:
            from_node_id = get_node_id(business_id=dto.document_id, node_label="Document")

        edges.append(
            ContainEdge(
                from_node_id=from_node_id,
                to_node_id=get_node_id(business_id=dto.part_id, node_label="Part"),
                edge_type="CONTAIN",
                created_at=get_current_timestamp()
            )
        )
    
    return nodes, edges


def mini_part_dtos_to_graph(mini_part_dtos: list[MiniPartDto]) -> tuple[list[Node], list[Edge]]:
    nodes: list[Node] = []
    edges: list[Edge] = []

    if len(mini_part_dtos):
        return nodes, edges

    for dto in mini_part_dtos:
        nodes.append(
            MiniPartNode(
                node_id=get_node_id(business_id=dto.mini_part_id, node_label="MiniPart"),
                node_label="MiniPart",
                created_at=get_current_timestamp(),
                source="legal_document",
                mini_part_id=dto.mini_part_id,
                mini_part_number=dto.mini_part_number,
                mini_part_name=dto.mini_part_name
            )
        )

        if dto.part_id is not None:
            from_node_id = get_node_id(business_id=dto.part_id, node_label="Part")
        else:
            from_node_id = get_node_id(business_id=dto.document_id, node_label="Document")

        edges.append(
            ContainEdge(
                from_node_id=from_node_id,
                to_node_id=get_node_id(business_id=dto.mini_part_id, node_label="MiniPart"),
                edge_type="CONTAIN",
                created_at=get_current_timestamp()
            )
        )
    
    return nodes, edges


def article_dtos_to_graph(article_dtos: list[ArticleDto]) -> tuple[list[Node], list[Edge]]:
    nodes: list[Node] = []
    edges: list[Edge] = []

    if len(article_dtos) == 0:
        return nodes, edges

    for dto in article_dtos:
        nodes.append(
            ArticleNode(
                node_id=get_node_id(business_id=dto.article_id, node_label="Article"),
                node_label="Article",
                created_at=get_current_timestamp(),
                source="legal_document",
                article_id=dto.article_id,
                article_number=dto.article_number,
                article_name=dto.article_name,
                article_content=dto.article_content,
                appendix_number=dto.appendix_number,
                effective_date=dto.effective_date
            )
        )

        if dto.mini_part_id is not None:
            from_node_id = get_node_id(business_id=dto.mini_part_id, node_label="MiniPart")
        elif dto.part_id is not None:
            from_node_id = get_node_id(business_id=dto.part_id, node_label="Part")
        elif dto.chapter_id is not None:
            from_node_id = get_node_id(business_id=dto.chapter_id, node_label="Chapter")
        elif dto.big_part_id is not None:
            from_node_id = get_node_id(business_id=dto.big_part_id, node_label="BigPart")
        else:
            from_node_id = get_node_id(business_id=dto.document_id, node_label="Document")
        
        edges.append(
            ContainEdge(
                from_node_id=from_node_id,
                to_node_id=get_node_id(business_id=dto.article_id, node_label="Article"),
                edge_type="CONTAIN",
                created_at=get_current_timestamp()
            )
        )
    
    return nodes, edges


def document_mapping_dtos_to_graph(document_mapping_dtos: list[DocumentMappingDto]) -> tuple[list[Node], list[Edge]]:
    nodes: list[Node] = []
    edges: list[Edge] = []

    if len(document_mapping_dtos) == 0:
        return nodes, edges

    for dto in document_mapping_dtos:
        nodes.append(
            DocumentNode(
                node_id=get_node_id(business_id=dto.from_document_id, node_label="Document"),
                node_label="Document",
                created_at=get_current_timestamp(),
                source="legal_document",
                document_id=dto.from_document_id,
                document_number=dto.from_document_number,
                document_name=dto.from_document_name,
                issued_date=dto.from_issued_date,
                effective_date=dto.from_effective_date,
                expiry_date=dto.from_expiry_date,
                status=dto.from_status,
                small_node=dto.from_small_note
            )
        )

        nodes.append(
            DocumentNode(
                node_id=get_node_id(business_id=dto.to_document_id, node_label="Document"),
                node_label="Document",
                created_at=get_current_timestamp(),
                source="legal_document",
                document_id=dto.to_document_id,
                document_number=dto.to_document_number,
                document_name=dto.to_document_name,
                issued_date=dto.to_issued_date,
                effective_date=dto.to_effective_date,
                expiry_date=dto.to_expiry_date,
                status=dto.to_status,
                small_node=dto.to_small_note
            )
        )

        from_node_id = get_node_id(business_id=dto.from_document_id, node_label="Document")
        to_node_id = get_node_id(business_id=dto.to_document_id, node_label="Document")
        
        if dto.relationship_type == "huong_dan":
            edges.append(
                GuideEdge(
                    from_node_id=from_node_id,
                    to_node_id=to_node_id,
                    edge_type="GUIDE",
                    created_at=get_current_timestamp(),
                    document_mapping_id=dto.mapping_id
                )
            )
        elif dto.relationship_type == "sua_doi":
            edges.append(
                AmendEdge(
                    from_node_id=from_node_id,
                    to_node_id=to_node_id,
                    edge_type="AMEND",
                    created_at=get_current_timestamp(),
                    document_mapping_id=dto.mapping_id
                )
            )
        elif dto.relationship_type == "thay_the":
            edges.append(
                ReplaceEdge(
                    from_node_id=from_node_id,
                    to_node_id=to_node_id,
                    edge_type="REPLACE",
                    created_at=get_current_timestamp(),
                    document_mapping_id=dto.mapping_id
                )
            )
        elif dto.relationship_type == "dinh_chinh":
            edges.append(
                CorrectEdge(
                    from_node_id=from_node_id,
                    to_node_id=to_node_id,
                    edge_type="CORRECT",
                    created_at=get_current_timestamp(),
                    document_mapping_id=dto.mapping_id
                )
            )
        elif dto.relationship_type == "hop_nhat":
            edges.append(
                ConsolidateEdge(
                    from_node_id=from_node_id,
                    to_node_id=to_node_id,
                    edge_type="CONSOLIDATE",
                    created_at=get_current_timestamp(),
                    document_mapping_id=dto.mapping_id
                )
            )
    
    return nodes, edges


def article_version_dtos_to_graph(article_version_dtos: list[ArticleVersionDto]) -> tuple[list[Node], list[Edge]]:
    nodes: list[Node] = []
    edges: list[Edge] = []

    if len(article_version_dtos) == 0:
        return nodes, edges

    last_versions: dict[str, str] = {}

    for dto in article_version_dtos:
        nodes.append(
            ArticleNode(
                node_id=get_node_id(business_id=dto.from_article_id, node_label="Article"),
                node_label="Article",
                created_at=get_current_timestamp(),
                source="legal_document",
                article_id=dto.from_article_id,
                article_number=dto.from_article_number,
                article_name=dto.from_article_name,
                article_content=dto.from_article_content,
                appendix_number=dto.from_appendix_number,
                effective_date=dto.from_effective_date
            )
        )

        nodes.append(
            ArticleNode(
                node_id=get_node_id(business_id=dto.to_article_id, node_label="Article"),
                node_label="Article",
                created_at=get_current_timestamp(),
                source="legal_document",
                article_id=dto.to_article_id,
                article_number=dto.to_article_number,
                article_name=dto.to_article_name,
                article_content=dto.to_article_content,
                appendix_number=dto.to_appendix_number,
                effective_date=dto.to_effective_date
            )
        )

        if dto.modification_type == "SĐ":
            amending_node_id = get_node_id(business_id=dto.from_article_id, node_label="Article")
            amended_node_id = get_node_id(business_id=dto.to_article_id, node_label="Article")
            new_version_node_id = get_node_id(business_id=dto.version_id, node_label="Article")

            nodes.append(
                ArticleNode(
                    node_id=new_version_node_id,
                    node_label="Article",
                    created_at=get_current_timestamp(),
                    source="legal_document",
                    article_id=dto.version_id,
                    article_number=dto.from_article_number,
                    article_name=dto.from_article_name,
                    article_content=dto.modification_content,
                    appendix_number=dto.from_appendix_number,
                    effective_date=dto.from_effective_date
                )
            )

            if last_versions.get(amended_node_id) is None:
                edges.append(
                    ImplementAmendmentEdge(
                        from_node_id=amending_node_id,
                        to_node_id=new_version_node_id,
                        edge_type="IMPLEMENT_AMENDMENT",
                        created_at=get_current_timestamp(),
                        version_id=dto.version_id,
                        from_date=dto.from_date,
                        to_date=dto.to_date,
                        is_abolish_previous_content=dto.is_abolish_previous_content
                    )
                )

                edges.append(
                    IsAmendedToEdge(
                        from_node_id=amended_node_id,
                        to_node_id=new_version_node_id,
                        edge_type="IS_AMENDED_TO",
                        created_at=get_current_timestamp()
                    )
                )
            else:
                edges.append(
                    ImplementAmendmentEdge(
                        from_node_id=amending_node_id,
                        to_node_id=new_version_node_id,
                        edge_type="IMPLEMENT_AMENDMENT",
                        created_at=get_current_timestamp(),
                        version_id=dto.version_id,
                        from_date=dto.from_date,
                        to_date=dto.to_date,
                        is_abolish_previous_content=dto.is_abolish_previous_content
                    )
                )

                edges.append(
                    IsAmendedToEdge(
                        from_node_id=last_versions.get(amended_node_id),
                        to_node_id=new_version_node_id,
                        edge_type="IS_AMENDED_TO",
                        created_at=get_current_timestamp()
                    )
                )
            
            last_versions[amended_node_id] = new_version_node_id
    
    return nodes, edges


def document_to_graph(document_data: DocumentData) -> tuple[list[Node], list[Edge]]:
    try:
        nodes: list[Node] = []
        edges: list[Edge] = []

        mappers = [
            (document_dto_to_graph, document_data.document_dto),
            (big_part_dtos_to_graph, document_data.big_part_dtos),
            (chapter_dtos_to_graph, document_data.chapter_dtos),
            (part_dtos_to_graph, document_data.part_dtos),
            (mini_part_dtos_to_graph, document_data.mini_part_dtos),
            (article_dtos_to_graph, document_data.article_dtos),
            (document_mapping_dtos_to_graph, document_data.document_mapping_dtos),
            (article_version_dtos_to_graph, document_data.article_version_dtos),
        ]

        for func, data in mappers:
            n, e = func(data)
            nodes.extend(n)
            edges.extend(e)

        return nodes, edges
    except Exception:
        raise
