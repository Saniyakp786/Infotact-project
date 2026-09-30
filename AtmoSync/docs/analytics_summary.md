# AtmoSync Analytics Summary

## 1. KPIs

The AtmoSync analytics engine calculates important Key Performance Indicators (KPIs) from the intermodal rail transportation dataset.

### Main KPIs

- Total Shipments
- Average Spoilage Risk
- Average Temperature
- Average Humidity
- Average Remaining Shelf Life
- Average Thermal Leakage

These KPIs provide a quick overview of shipment and environmental conditions.

---

## 2. Risk Classification

The analytics engine classifies shipments into three risk categories based on spoilage risk percentage.

| Spoilage Risk | Classification |
|---|---|
| Below 40% | LOW |
| 40% to 69% | MEDIUM |
| 70% and above | HIGH |

This classification helps identify shipments that may require additional monitoring.

> Note: These thresholds are project-defined rules for the AtmoSync analytics engine.

---

## 3. Alerts

The alert engine identifies potentially risky shipment conditions.

### Alert Rules

- Spoilage Risk >= 70% → HIGH_SPOILAGE_RISK
- Remaining Shelf Life <= 2 days → LOW_SHELF_LIFE
- Thermal Leakage >= 70 → THERMAL_LEAKAGE
- Temperature >= 30°C → TEMPERATURE_ALERT

These rules are used to flag shipments requiring attention.

> Note: Alert thresholds are project-defined rules and are not presented as universal scientific limits.

---

## 4. Spoilage Arbitrage

The Spoilage Arbitrage engine combines spoilage risk and remaining shelf life to suggest an operational action.

### Decision Rules

| Spoilage Risk | Shelf Life | Action |
|---|---|---|
| >= 70% | <= 2 days | URGENT_REROUTE |
| >= 40% | <= 2 days | CONSIDER_REROUTE |
| Otherwise | Any | NORMAL |

The purpose of this logic is to identify shipments where rerouting may be considered based on the project's defined risk and shelf-life rules.

---

## 5. Analytics Engine Flow

```text
                 AtmoSync Dataset
                        │
                        ▼
               ┌─────────────────┐
               │ Analytics Engine│
               └─────────────────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
         KPI           Risk          Alerts
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                  Arbitrage
                        │
                        ▼
                 Action Recommendation