from pydantic import BaseModel
from datetime import datetime


class Node(BaseModel):
    node_id: str
    node_label: str
    created_at: datetime
    source: str
    