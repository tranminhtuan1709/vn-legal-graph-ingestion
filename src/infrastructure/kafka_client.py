from confluent_kafka import Consumer
from typing import Any


class KafkaClient:
    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config

        try:
            self.consumer = Consumer(
                {
                    "bootstrap.servers": f"{self.config.get("host")}:{self.config.get("port")}",
                    "group.id": self.config.get("group_id"),
                    "auto.offset.reset": self.config.get("auto_offset_reset"),
                    "enable.auto.commit": self.config.get("enable_auto_commit"),
                    "allow.auto.create.topics": self.config.get("allow_auto_create_topics"),
                    "max.partition.fetch.bytes": self.config.get("max_partition_fetch_bytes"),
                    "fetch.max.bytes": self.config.get("fetch_max_bytes")
                }
            )

            self.consumer.subscribe(topics=self.config.get("topics"))
        except Exception:
            raise
    