import os
import json
import uuid
from confluent_kafka import Producer
from datetime import datetime
from zoneinfo import ZoneInfo


def get_current_timestamp() -> str:
    timezone = ZoneInfo("Asia/Ho_Chi_Minh")
    current_timestamp = datetime.now(timezone)

    return current_timestamp.strftime("%Y-%m-%d %H:%M:%S")


producer = Producer(
    {
        "bootstrap.servers": "localhost:9093"
    }
)

producer.produce(
    topic="approved_documents",
    value=json.dumps(
        {
            "message_id": uuid.uuid4().__str__(),
            "event_type": "document_approval",
            "timestamp": get_current_timestamp(),
            "source": "tool_review",
            "document_id": 36139
        }
    ).encode()
)

producer.flush()
print("Sent to Kafka successfully!")
