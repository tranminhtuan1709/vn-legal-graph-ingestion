from src.interface.dtos.internal.graph.base_node import BaseNode


class IssuingAuthorityNode(BaseNode):
    def __init__(
        self,
        issuing_authority_id: int,
        issuing_authority_name: str
    ) -> None:
        self.issuing_authority_id = issuing_authority_id
        self.issuing_authority_name = issuing_authority_name
