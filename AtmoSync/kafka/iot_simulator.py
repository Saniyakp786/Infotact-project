import random
import time
import json
from datetime import datetime


CONTAINERS = [
    "AIR-CNT001",
    "AIR-CNT002",
    "AIR-CNT003",
    "AIR-CNT004",
    "AIR-CNT005"
]


def generate_sensor_data():

    return {
        "container_id": random.choice(CONTAINERS),
        "timestamp": datetime.now().isoformat(),
        "temperature_celsius": round(random.uniform(2, 12), 2),
        "humidity_percentage": round(random.uniform(60, 95), 2),
        "vibration_level": round(random.uniform(0.1, 1.0), 2),
        "pressure_kpa": round(random.uniform(95, 105), 2)
    }


if __name__ == "__main__":

    while True:

        data = generate_sensor_data()

        print(json.dumps(data))

        time.sleep(2)