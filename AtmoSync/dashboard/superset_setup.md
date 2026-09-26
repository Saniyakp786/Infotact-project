# AtmoSync Air Freight - Superset Setup

## Data Flow

Snowflake
   ↓
dbt Models
   ↓
Apache Superset
   ↓
Air Freight Analytics Dashboard

## Snowflake Database

Database:
ATMOSYNC_DB

Schema:
RAW

## dbt Datasets

### 1. int_spoilage_analysis

Purpose:
Analyze shipment-level spoilage risk, shelf life, and environmental conditions.

### 2. fct_at_risk_containers

Purpose:
Identify shipments with high spoilage risk or low remaining shelf life.

Filter:
- spoilage_risk_percent >= 50
- OR remaining_shelf_life_days <= 5

### 3. fct_spoilage_arbitrage

Purpose:
Recommend shipment actions based on spoilage risk and remaining shelf life.

Recommended Actions:
- Urgent Reroute
- Reroute
- Monitor

## Superset Connection

Connect Apache Superset to Snowflake using:

Database: ATMOSYNC_DB
Schema: RAW

Datasets:
- int_spoilage_analysis
- fct_at_risk_containers
- fct_spoilage_arbitrage