# Day 27 — Final Analytics Models

## fct_spoilage_risk

This model provides shipment-level spoilage risk analysis.

Columns include:
- Shipment ID
- Recorded datetime
- Origin location
- Destination location
- Cargo type
- Temperature
- Humidity
- Vibration
- Thermal leakage
- Spoilage risk
- Remaining shelf life
- Spoilage status
- Risk category

Risk categories:
- Low: spoilage risk below 40%
- Medium: spoilage risk from 40% to 69%
- High: spoilage risk 70% or above

## fct_route_risk

This model provides route-level spoilage risk analysis.

Columns include:
- Origin location
- Destination location
- Shipment count
- Average spoilage risk
- Average shelf life

The final analytics models are ready for the BI layer.