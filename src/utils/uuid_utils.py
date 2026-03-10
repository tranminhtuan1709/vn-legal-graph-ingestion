import uuid
import os


def get_node_id(business_id: int, node_label: str) -> str:
    return uuid.uuid5(
        namespace=os.getenv("UUID_NAMESPACE"),
        name=f"{node_label}_{business_id}"
    ).__str__()
