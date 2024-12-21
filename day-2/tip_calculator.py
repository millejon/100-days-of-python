def add_tip(bill: float, percentage: float) -> float:
    """Return cost of bill after adding tip.

    Arguments:
        bill -- Cost of bill before tip
        percentage -- Tip percentage to add

    Returns:
        Cost of bill after tip
    """
    return round(bill * (1 + percentage / 100), 2)


def calculate_bill() -> float:
    """Return total cost of bill calculated from user input."""
    bill = float(input("How much is the bill?\n$"))
    percentage = float(input("What percentage would you like to tip? 15, 18, or 20?\n"))

    return add_tip(bill, percentage)


def calculate_share_of_bill() -> float:
    """Return share of bill calculated from user input."""
    bill = calculate_bill()
    people = int(input("How many people are splitting the bill?\n"))

    return round(bill / people, 2)


if __name__ == "__main__":
    print("Welcome to the tip calculator!")
    print(f"Each person should pay ${calculate_share_of_bill():.2f}.")
