\# Day 25 - Snowflake Setup



\## Overview



Snowflake was configured as the cloud data warehouse for the AtmoSync Intermodal Rail project.



\## Snowflake Structure



\- Database: ATMOSYNC

\- Schema: RAW

\- Table: INTERMODAL\_RAIL



\## Purpose



The Snowflake environment is used to store and manage the cleaned Intermodal Rail sensor dataset for analytics and downstream processing.



\## Data Flow



CSV Dataset → Snowflake RAW Schema → INTERMODAL\_RAIL Table → Analytics / dbt → Power BI



\## Day 25 Completion



\- Snowflake account configured

\- ATMOSYNC database created

\- RAW schema created

\- INTERMODAL\_RAIL table created

\- Dataset loaded into Snowflake

\- Snowflake environment verified



\## Next Step



Day 26 will focus on dbt setup and transformation models.

