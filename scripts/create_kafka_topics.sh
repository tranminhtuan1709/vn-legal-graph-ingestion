#!/bin/bash

/opt/kafka/bin/kafka-topics.sh \
    --create \
    --if-not-exists \
    --topic approved_documents \
    --bootstrap-server kafka:9092 \
    --partitions 1 \
    --replication-factor 1
