import uuid
import os


def get_node_id(business_id: int, node_label: str) -> str:
    namespace = uuid.UUID(os.getenv("UUID_NAMESPACE"))

    return str(uuid.uuid5(
        namespace=namespace,
        name=f"{node_label}_{business_id}"
    ))
