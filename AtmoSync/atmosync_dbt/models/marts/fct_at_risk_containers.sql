SELECT
    shipment_id,
    transport_mode,
    origin_location,
    destination_location,
    cargo_type,
    temperature_celsius,
    humidity_percentage,
    spoilage_risk_percent,
    remaining_shelf_life_days,
    risk_category,
    shelf_life_category,
    spoilage_status

FROM {{ ref('int_spoilage_analysis') }}

WHERE spoilage_risk_percent >= 50
   OR remaining_shelf_life_days <= 5