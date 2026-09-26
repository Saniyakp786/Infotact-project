SELECT
    shipment_id,
    transport_mode,
    origin_location,
    destination_location,
    cargo_type,
    spoilage_risk_percent,
    remaining_shelf_life_days,
    risk_category,

    CASE
        WHEN spoilage_risk_percent >= 75
             AND remaining_shelf_life_days <= 2
            THEN 'Urgent Reroute'

        WHEN spoilage_risk_percent >= 50
             OR remaining_shelf_life_days <= 5
            THEN 'Reroute'

        ELSE 'Monitor'
    END AS recommended_action

FROM {{ ref('int_spoilage_analysis') }}