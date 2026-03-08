from confluent_kafka import Consumer

from src.configs.kafka_config import KafkaConfig
from src.exceptions.custom_exceptions import InfrastructureError


class KafkaClient:
    def __init__(self, config: KafkaConfig) -> None:
        self.config = config
    
    def get_consumer(self):
        try:
            consumer = Consumer(config={
                "bootstrap.servers": f"{self.config.host}:{self.config.port}",
                "group.id": self.config.group_id,
                "auto.offset.reset": self.config.auto_offset_reset,
                "enable.auto.commit": self.config.enable_auto_commit,
                "allow.auto.create.topics": self.config.allow_auto_create_topics,
                "max.partition.fetch.bytes": self.config.max_partition_fetch_bytes,
                "fetch.max.bytes": self.config.fetch_max_bytes
            })

            consumer.subscribe(topics=[self.config.topics])

            return consumer
        except Exception as e:
            raise InfrastructureError(
                message="Failed to create Kafka Consumer",
                context={
                    "host": self.config.host,
                    "port": self.config.port,
                    "username": self.config.username,
                    "topic": self.config.topics,
                    "group.id": self.config.group_id,
                    "auto_offset_reset": self.config.auto_offset_reset,
                    "enable_auto_commit": self.config.enable_auto_commit,
                    "allow_auto_create_topics": self.config.allow_auto_create_topics,
                    "max_partition_fetch_bytes": self.config.max_partition_fetch_bytes,
                    "fetch_max_bytes": self.config.fetch_max_bytes
                }
            ) from e
