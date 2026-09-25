import json
import time

from kafka import KafkaProducer

from iot_simulator import generate_sensor_data


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


TOPIC = "atmosync-telemetry"

print("Kafka Producer started...")


while True:

    data = generate_sensor_data()

    producer.send(
        TOPIC,
        value=data
    )

    print("Sent:", data)

    time.sleep(1)