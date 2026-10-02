# Day 24 — At-Risk Model

## Objective
Create a dbt mart model to identify at-risk shipments.

## Model
atmosync_dbt/models/marts/fct_at_risk_containers.sql

## Work Completed
- Selected shipment and environmental details.
- Included spoilage risk and remaining shelf life.
- Filtered shipments where spoilage risk is 50% or higher.
- Included shipments with remaining shelf life of 5 days or less.
- Used int_spoilage_analysis as the source.

## Status
The SQL model already exists and was committed earlier.