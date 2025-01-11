def add_tip(bill: float, percentage: float) -> float:
    """Add a tip to a bill.

    Arguments:
        bill -- The cost of the bill before tip
        percentage -- The tip percentage to add

    Returns:
        Total cost of the bill after tip
    """
    return round(bill * (1 + percentage / 100), 2)


def split_bill(bill: float, people: int) -> float:
    """Calculate each person's share of the bill.

    Arguments:
        bill -- The cost of the bill
        people -- The number of people in the party

    Returns:
        Amount each person should pay
    """
    return round(bill / people, 2)


def restaurant_bill_calculator() -> None:
    """Add a tip to the bill and calculate each person's share."""
    print("Welcome to the restaurant bill calculator!")

    bill = float(input("How much is the bill?\n$"))
    percentage = float(input("What percentage would you like to tip? 15, 18, or 20?\n"))
    people = int(input("How many people are splitting the bill?\n"))

    print(
        f"Each person should pay ${split_bill(add_tip(bill, percentage), people):.2f}."
    )


if __name__ == "__main__":
    restaurant_bill_calculator()
