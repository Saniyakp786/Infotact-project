# Day 23 — Spoilage Analytics

## Objective
Build an intermediate dbt model for shipment spoilage analytics.

## Model
atmosync_dbt/models/intermediate/int_spoilage_analysis.sql

## Work Completed
- Added risk categories: Critical, High, Medium, Low.
- Added shelf-life categories: Critical, At Risk, Safe.
- Selected shipment, cargo, environmental, spoilage-risk, and shelf-life fields.
- Used stg_shipments as the source through dbt ref.

## Status
The SQL model already exists and was committed earlier.