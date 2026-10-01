def determine_action(spoilage_risk, shelf_life):

    if spoilage_risk >= 70 and shelf_life <= 2:
        return "URGENT_REROUTE"

    elif spoilage_risk >= 40 and shelf_life <= 2:
        return "CONSIDER_REROUTE"

    else:
        return "NORMAL"


if __name__ == "__main__":

    test_cases = [
        (80, 1),
        (60, 2),
        (30, 5)
    ]

    for risk, shelf_life in test_cases:

        action = determine_action(
            risk,
            shelf_life
        )

        print(
            f"Risk={risk}%, "
            f"Shelf Life={shelf_life} days "
            f"→ {action}"
        )