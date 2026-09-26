SELECT
    shipment_id,
    transport_mode,
    recorded_date,
    recorded_time,
    recorded_datetime,
    origin_location,
    destination_location,
    cargo_type,
    temperature_celsius,
    humidity_percentage,
    vibration_level,
    pressure_kpa,
    exposure_duration_hours,
    door_open_count,
    salinity_ppt,
    thermal_leakage_score,
    spoilage_risk_percent,
    remaining_shelf_life_days,
    spoilage_status

FROM {{ source('raw', 'RAW_SHIPMENTS') }}