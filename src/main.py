import json
import os
from dotenv import load_dotenv
from typing import Any

from configs.kafka_config import KafkaConfig
from configs.mysql_config import MySQLConfig
from configs.neo4j_config import Neo4jConfig

from infrastructure.kafka_client import KafkaClient
from infrastructure.mysql_client import MySQLClient
from infrastructure.neo4j_client import Neo4jClient

from interface.validators.document_validator import DocumentValidator
from interface.normalizers.document_normalizer import DocumentNormalizer

from repositories.document_repository import DocumentRepository
from repositories.graph_repository import GraphRepository

from services.document_service import DocumentService
from utils.logger import logger

load_dotenv(dotenv_path="./.env")

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

logger.info("Consumer started")

while True:
    try:
        message = kafka_client.consumer.poll(timeout=1.0)

        if message is None or message.value() is None:
            continue
        
        if message.error():
            raise
        
        topic = message.topic()
        logger.info(msg=f"Received a message from topic {topic}: {message.value()}")
        message_value: dict[str, Any] = json.loads(message.value().decode())

        if topic == "approved_documents":
            document_id: int = message_value.get("document_id")
            document_service.ingest_document(document_id=document_id)
            logger.info(msg=f"Ingested document ID: {document_id}")
            logger.info(msg=f"\n\n{'=' * 100}\n\n")
    except Exception as e:
        logger.error(msg=f"Failed to ingest", exc_info=True)
        logger.info(msg=f"\n\n\n{'=' * 100}\n\n\n")
        break
    finally:
        kafka_client.consumer.commit()
