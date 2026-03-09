from confluent_kafka import Consumer

from configs.kafka_config import KafkaConfig


class KafkaClient:
    def __init__(self, config: KafkaConfig) -> None:
        self.config = config

        try:
            self.consumer = Consumer(
                {
                    "bootstrap.servers": f"{self.config.host}:{self.config.port}",
                    "group.id": self.config.group_id,
                    "auto.offset.reset": self.config.auto_offset_reset,
                    "enable.auto.commit": self.config.enable_auto_commit,
                    "allow.auto.create.topics": self.config.allow_auto_create_topics,
                    "max.partition.fetch.bytes": self.config.max_partition_fetch_bytes,
                    "fetch.max.bytes": self.config.fetch_max_bytes
                }
            )

            self.consumer.subscribe(topics=self.config.topics)
        except Exception:
            raise
