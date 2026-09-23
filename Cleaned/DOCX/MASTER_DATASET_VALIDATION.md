# AtmoSync Master Dataset – Cleaning & Validation

## 1. Dataset Preparation
- Combined the cleaned datasets into one Master Dataset.
- Checked the overall dataset structure and columns.
- Standardized column names.

## 2. Data Cleaning
- Removed duplicate Shipment IDs.
- Checked missing/blank values.
- Removed unwanted spaces from text values.
- Standardized Transport Mode:
  Air, Sea, Truck, Rail.
- Standardized Spoilage Status values.
- Corrected Date and Time format.
- Checked numeric columns for incorrect values.

## 3. Data Validation
- Checked whether each Shipment ID is unique.
- Checked missing values in important columns.
- Checked inconsistent spellings and extra spaces.
- Checked temperature, humidity and vibration values.
- Checked categorical and numeric columns separately.
- Verified that the dataset structure is consistent.

## 4. Excel Formulas Used for Checking

### Missing Values
COUNTBLANK() was used to find empty cells.

Example:
=COUNTBLANK(A:A)

### Duplicate Shipment IDs
COUNTIF() was used to check repeated Shipment IDs.

Example:
=COUNTIF(A:A,A2)

If the result is greater than 1, the ID is repeated.

### Remove Extra Spaces
TRIM() was used to remove unwanted spaces.

Example:
=TRIM(A2)

### Check Missing Data
IF() was used to identify missing values.

Example:
=IF(A2="","Missing","OK")

### Multiple Condition Check
COUNTIFS() was used to check data based on multiple conditions.

## 5. Final Check
- Checked the cleaned Master Dataset again.
- Verified important columns and values.
- Confirmed that the dataset is ready for Power BI analysis.