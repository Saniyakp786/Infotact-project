def generate_alerts(row):

    alerts = []

    if row["spoilage_risk_percent"] >= 70:
        alerts.append("HIGH_SPOILAGE_RISK")

    if row["remaining_shelf_life_days"] <= 2:
        alerts.append("LOW_SHELF_LIFE")

    if row["thermal_leakage_score"] >= 70:
        alerts.append("THERMAL_LEAKAGE")

    if row["temperature_celsius"] >= 30:
        alerts.append("TEMPERATURE_ALERT")

    return alerts


if __name__ == "__main__":

    import pandas as pd

    df = pd.read_csv(
        "../data/Cleaned_Dataset_IntermodalRail.csv"
    )

    print("AtmoSync Alert Engine")
    print("---------------------")

    for _, row in df.iterrows():

        alerts = generate_alerts(row)

        if alerts:

            print(
                f"\nShipment: {row['shipment_id']}"
            )

            print(
                f"Risk: {row['spoilage_risk_percent']:.2f}%"
            )

            print(
                f"Shelf Life: "
                f"{row['remaining_shelf_life_days']} days"
            )

            print(
                "Alerts:",
                ", ".join(alerts)
            )