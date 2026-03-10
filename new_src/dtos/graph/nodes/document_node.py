from dtos.graph.nodes.node import Node


class DocumentNode(Node):
    document_id: int
    document_number: str | None
    document_name: str | None
    issued_date: str | None
    effective_date: str | None
    expiry_date: str | None
    status: str | None
    small_node: str | None
    