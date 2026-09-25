import json

from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "atmosync-telemetry",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)


print("Kafka Consumer started...")


for message in consumer:

    print("Received:", message.value)