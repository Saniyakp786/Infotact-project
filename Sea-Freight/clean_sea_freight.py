import pandas as pd
import numpy as np

df = pd.read_csv('Sea-Freight/AtmoSync_Route_SeaFreight.csv')

# ===== PHASE 1: EXPLORE =====
print(df.head())
# getting to know my first few rows and how they look

print(df.info())
# total columns with names and datatypes

print(df.shape)
# total counts of rows and columns (262, 18)

print(df.isnull().sum())
# total missing values we have in each column

print(df.duplicated().sum())
# count of total duplicate rows

print(df[df.duplicated(keep=False)])
# displays all the duplicate rows and columns

print(df.describe())
# displays all statistical calculations of numeric values
# ex: count, mean, std, min, max

print(df['spoilage_status'].unique())
print(df['cargo_type'].unique())
print(df['transport_mode'].unique())
# finding the values present in each column
# helps identify spelling mistakes, spacing, capitalization

# ===== PHASE 3: VALIDATE (prove each issue exists) =====
print(df[(df['humidity_percentage'] < 0) | (df['humidity_percentage'] > 100)][['shipment_id', 'humidity_percentage']])
print(df[df['vibration_level'] < 0][['shipment_id', 'vibration_level']])

# ===== PHASE 4: FIX (one at a time) =====

# Fix 1: text formatting (spacing + capitalization)
df['transport_mode'] = df['transport_mode'].str.strip().str.title()
df['spoilage_status'] = df['spoilage_status'].str.strip().str.title()

# Fix 2: correct the typo
df['transport_mode'] = df['transport_mode'].replace({'Sea Frieght': 'Sea Freight'})
print(df['transport_mode'].unique())
print(df['spoilage_status'].unique())

# Fix 3: convert placeholder text into real missing values
placeholder_values = ['N/A', 'NA', 'null', '-', 'unknown']
df['cargo_type'] = df['cargo_type'].replace(placeholder_values, np.nan)
print(df['cargo_type'].isnull().sum())

# Fix 4: handle missing values
before = len(df)
df = df.dropna(subset=['temperature_celsius', 'humidity_percentage'])
after = len(df)
print(f"Dropped {before - after} rows missing critical sensor readings.")

if df['cargo_type'].isnull().sum() > 0:
    most_common_cargo = df['cargo_type'].mode()[0]
    df['cargo_type'] = df['cargo_type'].fillna(most_common_cargo)
    print(f"Filled remaining missing cargo_type with: '{most_common_cargo}'")

print(df.isnull().sum())

# Fix 5: negative values
df['humidity_percentage'] = df['humidity_percentage'].abs()
df['vibration_level'] = df['vibration_level'].abs()
print("Negative humidity:", (df['humidity_percentage'] < 0).sum())
print("Negative vibration:", (df['vibration_level'] < 0).sum())

# Fix 6: cap humidity above 100% (THIS WAS MISSING BEFORE)
df.loc[df['humidity_percentage'] > 100, 'humidity_percentage'] = 100
print("Still above 100:", (df['humidity_percentage'] > 100).sum())

# Fix 7: remove impossible outlier temperature (999)
df = df[df['temperature_celsius'] < 100]
print("Rows with impossible temp still remaining:", (df['temperature_celsius'] >= 100).sum())
print("Current row count:", len(df))

# Fix 8: standardize date format
df['recorded_date'] = pd.to_datetime(df['recorded_date'], format='mixed', dayfirst=True, errors='coerce')
df['recorded_date'] = df['recorded_date'].dt.strftime('%Y-%m-%d')
print(df['recorded_date'].head(10))

# Fix 9: remove exact duplicate rows
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Removed {before - after} duplicate row(s).")

# ===== PHASE 5: FINAL VALIDATION =====
print("=== FINAL CHECK ===")
print("Missing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nTemperature range:", df['temperature_celsius'].min(), "to", df['temperature_celsius'].max())
print("Humidity range:", df['humidity_percentage'].min(), "to", df['humidity_percentage'].max())
print("\nFinal row count:", len(df))
print("transport_mode values:", df['transport_mode'].unique())
print("spoilage_status values:", df['spoilage_status'].unique())




# ===== SAVE =====
df.to_csv('Sea-Freight/AtmoSync_Route_SeaFreight_CLEANED.csv', index=False)
print("\nSaved cleaned file.")