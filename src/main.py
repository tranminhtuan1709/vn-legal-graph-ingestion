import os
import json
from dotenv import load_dotenv

from infrastructure.kafka_client import KafkaClient
from infrastructure.mysql_client import MySQLClient
from infrastructure.neo4j_client import Neo4jClient

from pipelines.document_pipeline import DocumentPipeline

from utils.logger import logger

load_dotenv(dotenv_path="../.env")

kafka_client = KafkaClient(
    host=os.getenv("KAFKA_HOST"),
    port=int(os.getenv("KAFKA_PORT")),
    username=os.getenv("KAFKA_USERNAME"),
    password=os.getenv("KAFKA_PASSWORD"),
    group_id=os.getenv("KAFKA_GROUP_ID"),
    auto_offset_reset=os.getenv("KAFKA_AUTO_OFFSET_RESET"),
    enable_auto_commit=os.getenv("KAFKA_ENABLE_AUTO_COMMIT") == "true",
    allow_auto_create_topics=os.getenv("KAFKA_AUTO_CREATE_TOPICS") == "true",
    max_partition_fetch_bytes=int(os.getenv("KAFKA_MAX_PARTITION_FETCH_BYTES")),
    fetch_max_bytes=int(os.getenv("KAFKA_FETCH_MAX_BYTES")),
    topics=os.getenv("KAFKA_TOPICS").split(",")
)

mysql_client_document = MySQLClient(
    host=os.getenv("MYSQL_DOCUMENT_HOST"),
    port=int(os.getenv("MYSQL_DOCUMENT_PORT")),
    username=os.getenv("MYSQL_DOCUMENT_USERNAME"),
    password=os.getenv("MYSQL_DOCUMENT_PASSWORD"),
    database=os.getenv("MYSQL_DOCUMENT_DATABASE"),
    pool_name=os.getenv("MYSQL_POOL_NAME"),
    pool_size=int(os.getenv("MYSQL_POOL_SIZE")),
    connection_timeout=int(os.getenv("MYSQL_CONNECTION_TIMEOUT"))
)

neo4j_client = Neo4jClient(
    host=os.getenv("NEO4J_HOST"),
    port=int(os.getenv("NEO4J_PORT")),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
    database=os.getenv("NEO4J_DATABASE"),
    connection_timeout=int(os.getenv("NEO4J_CONNECTION_TIMEOUT")),
    max_connection_pool_size=int(os.getenv("NEO4J_MAX_CONNECTION_POOL_SIZE"))
)

document_pipeline = DocumentPipeline(mysql_client_document, neo4j_client)

logger.info("Consumer started")

while True:
    try:
        message = kafka_client.consumer.poll(timeout=1.0)

        if message is None or message.value() is None:
            continue

        if message.error():
            raise

        topic = message.topic()
        logger.info(f"Received a message from topic '{topic}': {message.value()}")
        message_value = json.loads(message.value())

        if topic == "approved_documents":
            document_pipeline.run(message_value.get("document_id"))
    except Exception:
        logger.error("An unexpected error occured", exc_info=True)
    finally:
        kafka_client.consumer.commit()
    