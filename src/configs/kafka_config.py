class KafkaConfig:
    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        topics: list[str],
        group_id: str,
        auto_offset_reset: str,
        enable_auto_commit: bool,
        allow_auto_create_topics: bool,
        max_partition_fetch_bytes: int,
        fetch_max_bytes: int
    ) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.topics = topics
        self.group_id = group_id
        self.auto_offset_reset = auto_offset_reset
        self.enable_auto_commit = enable_auto_commit
        self.allow_auto_create_topics = allow_auto_create_topics
        self.max_partition_fetch_bytes = max_partition_fetch_bytes
        self.fetch_max_bytes = fetch_max_bytes
