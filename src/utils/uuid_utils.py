import uuid


def get_node_id(namespace: str, node_id: int, node_label: str) -> str:
    return uuid.uuid5(
        namespace=namespace,
        name=f"{node_label}_{node_id}"
    ).__str__()
