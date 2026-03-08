import json
import os
import logging
from dotenv import load_dotenv

from src.configs.kafka_config import KafkaConfig
from src.configs.mysql_config import MySQLConfig
from src.configs.neo4j_config import Neo4jConfig

from src.infrastructure.kafka_client import KafkaClient
from src.infrastructure.mysql_client import MySQLClient
from src.infrastructure.neo4j_client import Neo4jClient

from src.interface.validators.document_validator import DocumentValidator
from src.interface.normalizers.document_normalizer import DocumentNormalizer

from src.repositories.document_repository import DocumentRepository
from src.repositories.graph_repository import GraphRepository

from src.services.document_service import DocumentService

from src.utils.logger import get_logger
from src.exceptions.custom_exceptions import CustomBaseError

load_dotenv(dotenv_path="/.env")

kafka_config = KafkaConfig(
    host=os.getenv("KAFKA_HOST"),
    port=int(os.getenv("KAFKA_PORT")),
    username=os.getenv("KAFKA_USERNAME"),
    password=os.getenv("KAFKA_PASSWORD"),
    topics=os.getenv("KAFKA_TOPICS").split(","),
    group_id=os.getenv("KAFKA_GROUP_ID"),
    auto_offset_reset=os.getenv("KAFKA_AUTO_OFFSET_RESET"),
    enable_auto_commit=os.getenv("KAFKA_ENABLE_AUTO_COMMIT") == "true",
    allow_auto_create_topics=os.getenv("KAFKA_ALLOW_AUTO_CREATE_TOPICS") == "true",
    max_partition_fetch_bytes=int(os.getenv("KAFKA_MAX_PARTITION_FETCH_BYTES")),
    fetch_max_bytes=int(os.getenv("KAFKA_FETCH_MAX_BYTES"))
)

mysql_config = MySQLConfig(
    host=os.getenv("MYSQL_DOCUMENT_HOST"),
    port=int(os.getenv("MYSQL_DOCUMENT_PORT")),
    username=os.getenv("MYSQL_DOCUMENT_USERNAME"),
    password=os.getenv("MYSQL_DOCUMENT_PASSWORD"),
    database=os.getenv("MYSQL_DOCUMENT_DATABASE"),
    pool_name=os.getenv("MYSQL_POOL_NAME"),
    pool_size=int(os.getenv("MYSQL_POOL_SIZE")),
    connection_timeout=int(os.getenv("MYSQL_CONNECTION_TIMEOUT"))
)

neo4j_config = Neo4jConfig(
    host=os.getenv("NEO4J_HOST"),
    port=int(os.getenv("NEO4J_PORT")),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
    database=os.getenv("NEO4J_DATABASE"),
    connection_timeout=int(os.getenv("NEO4J_CONNECTION_TIMEOUT")),
    max_connection_pool_size=int(os.getenv("NEO4J_MAX_CONNECTION_POOL_SIZE"))
)

kafka_client = KafkaClient(config=kafka_config)
mysql_client = MySQLClient(config=mysql_config)
neo4j_client = Neo4jClient(config=neo4j_config)

document_validator = DocumentValidator()
document_normalizer = DocumentNormalizer()

document_repository = DocumentRepository(
    mysql_client=mysql_client,
    document_validator=document_validator,
    document_normalizer=document_normalizer
)

graph_repository = GraphRepository(neo4j_client=neo4j_client)

document_service = DocumentService(
    document_repository=document_repository,
    graph_repository=graph_repository,
    uuid_namespace=os.getenv("UUID_NAMESPACE")
)

kafka_consumer = kafka_client.get_consumer()

log_level_mapping = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARN,
    "error": logging.ERROR
}

logger = get_logger(
    name=os.getenv("LOG_NAME"),
    log_file=os.getenv("LOG_FILE"),
    max_bytes=int(os.getenv("LOG_MAX_BYTES")),
    backup_count=int(os.getenv("LOG_BACKUP_COUNT")),
    level=log_level_mapping.get(os.getenv("LOG_LEVEL"))
)

while True:
    for topic in kafka_config.topics:
        try:
            message = kafka_consumer.poll(timeout=1.0)

            if message is None:
                logger.info(msg=f"Ignore a null message from topic {topic}")
            
            message_value: dict[str, any] = json.loads(message.value().decode(encoding="utf-8"))
            logger.info(msg=json.dumps(message_value))

            if topic == "approved_document_ids":
                document_service.ingest_document(document_id=message_value.get("document_id"))
        except CustomBaseError as e:
            logger.error(
                msg=str(e),
                exc_info=True,
                extra={
                    "context": e.context
                }
            )
        except Exception as e:
            logger.error(
                msg=f"An unexpected error occured while processing message from topic {topic}",
                exc_info=True
            )
