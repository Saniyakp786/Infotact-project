USE DATABASE ATMOSYNC_DB;

USE SCHEMA RAW;

CREATE OR REPLACE TABLE RAW_IOT_TELEMETRY (
    container_id VARCHAR,
    timestamp TIMESTAMP,
    temperature_celsius FLOAT,
    humidity_percentage FLOAT,
    vibration_level FLOAT,
    pressure_kpa FLOAT
);

CREATE OR REPLACE TABLE RAW_SHIPMENTS (
    shipment_id VARCHAR,
    transport_mode VARCHAR,
    recorded_date DATE,
    recorded_time VARCHAR,
    recorded_datetime TIMESTAMP,
    origin_location VARCHAR,
    destination_location VARCHAR,
    cargo_type VARCHAR,
    temperature_celsius FLOAT,
    humidity_percentage FLOAT,
    vibration_level FLOAT,
    pressure_kpa FLOAT,
    exposure_duration_hours FLOAT,
    door_open_count INTEGER,
    salinity_ppt FLOAT,
    thermal_leakage_score FLOAT,
    spoilage_risk_percent FLOAT,
    remaining_shelf_life_days FLOAT,
    spoilage_status VARCHAR
);