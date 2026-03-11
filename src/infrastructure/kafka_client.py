from confluent_kafka import Consumer


class KafkaClient:
    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        group_id: str,
        auto_offset_reset: str,
        enable_auto_commit: bool,
        allow_auto_create_topics: bool,
        max_partition_fetch_bytes: int,
        fetch_max_bytes: int,
        topics: list[str]
    ) -> None:

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.group_id = group_id
        self.auto_offset_reset = auto_offset_reset
        self.enable_auto_commit = enable_auto_commit
        self.allow_auto_create_topics = allow_auto_create_topics
        self.max_partition_fetch_bytes = max_partition_fetch_bytes
        self.fetch_max_bytes = fetch_max_bytes
        self.topics = topics

        try:
            self.consumer = Consumer(
                {
                    "bootstrap.servers": f"{self.host}:{self.port}",
                    "group.id": self.group_id,
                    "auto.offset.reset": self.auto_offset_reset,
                    "enable.auto.commit": self.enable_auto_commit,
                    "allow.auto.create.topics": self.allow_auto_create_topics,
                    "max.partition.fetch.bytes": self.max_partition_fetch_bytes,
                    "fetch.max.bytes": self.fetch_max_bytes
                }
            )

            self.consumer.subscribe(self.topics)
        except Exception:
            raise
