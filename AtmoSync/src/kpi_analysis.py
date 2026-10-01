import pandas as pd


def calculate_kpis(df):
    kpis = {
        "total_shipments": len(df),
        "average_spoilage_risk": df["spoilage_risk_percent"].mean(),
        "average_temperature": df["temperature_celsius"].mean(),
        "average_humidity": df["humidity_percentage"].mean(),
        "average_shelf_life": df["remaining_shelf_life_days"].mean(),
        "average_thermal_leakage": df["thermal_leakage_score"].mean()
    }

    return kpis


if __name__ == "__main__":

    df = pd.read_csv(
        "../data/Cleaned_Dataset_IntermodalRail.csv"
    )

    kpis = calculate_kpis(df)

    print("AtmoSync KPI Summary")
    print("--------------------")

    for name, value in kpis.items():
        print(f"{name}: {value:.2f}")