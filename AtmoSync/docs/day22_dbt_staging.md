# Day 22 - Air Freight dbt Staging Model

## Objective
Create a staging model for Air Freight shipment data using dbt.

## Model
`stg_shipments.sql`

## Source
`RAW_SHIPMENTS` from the `raw` source.

## Description
The staging model selects shipment details, transport information, environmental sensor readings, spoilage risk, remaining shelf life, and spoilage status from the raw Snowflake table.

## Validation
The SQL model was checked, and the dbt project was parsed successfully.