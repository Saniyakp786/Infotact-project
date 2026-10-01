import pandas as pd
import json
import time
from kafka import KafkaProducer

# Dataset path
CSV_PATH = "data/Cleaned_Dataset_IntermodalRail.csv"

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Read dataset
df = pd.read_csv(CSV_PATH)

print("AtmoSync Kafka Producer Started")
print(f"Total records: {len(df)}")

# Send each row to Kafka
for index, row in df.iterrows():

    message = row.to_dict()

    producer.send(
        "atmosync-rail-sensors",
        value=message
    )

    shipment_id = message.get("shipment_id", index + 1)

    print(f"Sent: {shipment_id}")

    time.sleep(1)

producer.flush()

print("All AtmoSync records sent successfully.")