from dtos.graph.nodes.node import Node
from datetime import date


class DocumentNode(Node):
    document_id: int
    document_number: str | None
    document_name: str | None
    issued_date: date | None
    effective_date: date | None
    expiry_date: date | None
    status: str | None
    small_node: str | None
    