from src.interface.dtos.internal.graph.base_edge import BaseEdge


class GuideEdge(BaseEdge):
    def __init__(self, document_mapping_id: int) -> None:
        self.document_mapping_id = document_mapping_id
