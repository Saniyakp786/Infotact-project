import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "atmosync-rail-sensors",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("================================")
print("      ATMO SYNC CONSUMER")
print("================================")
print("Waiting for sensor data...\n")

for message in consumer:
    data = message.value

    shipment_id = data.get("shipment_id", "N/A")
    temperature = data.get("temperature_celsius", "N/A")
    humidity = data.get("humidity_percentage", "N/A")
    risk = data.get("spoilage_risk_percent", "N/A")

    print("[ATMO SYNC]")
    print(f"Shipment    = {shipment_id}")
    print(f"Temperature = {temperature}")
    print(f"Humidity    = {humidity}")
    print(f"Risk        = {risk}")
    print("--------------------------------")