\# AtmoSync — End-to-End Architecture



\## Project Overview

AtmoSync monitors environmental conditions during transportation and analyzes their possible impact on agricultural cargo.



\## End-to-End Data Flow



1\. Dataset: Transport datasets are used as input.

2\. Jupyter: Python notebooks are used to inspect and process the data.

3\. Data Cleaning: Data quality, missing values, and data types are checked.

4\. EDA: Temperature, humidity, vibration, and other variables are explored.

5\. Python Analytics: Shipment and environmental KPIs are calculated.

6\. Risk Classification: Shipments are grouped into risk categories using project-defined rules.

7\. Alert Engine: Risk conditions are checked to identify shipments that may need attention.

8\. Kafka: Telemetry messages are streamed through Kafka.

9\. Snowflake: Data is stored for querying and analysis.

10\. dbt: Data is transformed into staging and analytics models.

11\. Merged Analytics Data: Transport datasets are combined for cross-mode analysis.

12\. Power BI: The Environmental Monitoring page displays KPIs, charts, and slicers.



\## Current Validation



\- Power BI Environmental Monitoring page created and saved.

\- Power BI transport mode slicer tested successfully.

\- dbt Rail models executed successfully.

\- Full end-to-end integration must be validated stage by stage.



\## Notes

Update this document if any pipeline stage is not yet connected or tested.

