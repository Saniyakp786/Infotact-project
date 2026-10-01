def classify_risk(risk):

    if risk < 40:
        return "LOW"

    elif risk < 70:
        return "MEDIUM"

    else:
        return "HIGH"


if __name__ == "__main__":

    test_values = [20, 45, 68, 75, 90]

    for risk in test_values:

        category = classify_risk(risk)

        print(
            f"Risk: {risk}% → {category}"
        )