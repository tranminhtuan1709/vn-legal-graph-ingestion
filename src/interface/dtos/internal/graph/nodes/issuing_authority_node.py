from interface.dtos.internal.graph.node import Node


class IssuingAuthorityNode(Node):
    def __init__(
        self,
        node_id: str,
        node_label: str,
        created_at: str,
        source: str,
        issuing_authority_id: int,
        issuing_authority_name: str
    ) -> None:
        super().__init__(
            node_id=node_id,
            node_label=node_label,
            created_at=created_at,
            source=source
        )

        self.issuing_authority_id = issuing_authority_id
        self.issuing_authority_name = issuing_authority_name
