# Day 25 — Spoilage Arbitrage

## Objective
Create an intermediate decision model for spoilage-related rerouting.

## Model
atmosync_dbt/models/marts/fct_spoilage_arbitrage.sql

## Work Completed
- Added recommended actions: Urgent Reroute, Reroute, and Monitor.
- Used spoilage risk and remaining shelf life to determine actions.
- Used int_spoilage_analysis as the source.
- No monetary arbitrage amount is calculated because market-price data is unavailable.

## Status
The SQL model already exists and was committed earlier.