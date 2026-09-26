SELECT
    shipment_id,
    transport_mode,
    origin_location,
    destination_location,
    cargo_type,
    temperature_celsius,
    humidity_percentage,
    vibration_level,
    exposure_duration_hours,
    thermal_leakage_score,
    spoilage_risk_percent,
    remaining_shelf_life_days,

    CASE
        WHEN spoilage_risk_percent >= 75 THEN 'Critical'
        WHEN spoilage_risk_percent >= 50 THEN 'High'
        WHEN spoilage_risk_percent >= 25 THEN 'Medium'
        ELSE 'Low'
    END AS risk_category,

    CASE
        WHEN remaining_shelf_life_days <= 2 THEN 'Critical'
        WHEN remaining_shelf_life_days <= 5 THEN 'At Risk'
        ELSE 'Safe'
    END AS shelf_life_category,

    spoilage_status

FROM {{ ref('stg_shipments') }}