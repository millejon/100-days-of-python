import os

import ascii_art as art


def secret_auction() -> None:
    """Run a secret auction."""
    print(art.logo)
    print("Welcome to the secret auction!")
    bids = {}
    bidding = True

    while bidding:
        name = input("What is your name?\n")
        bids[name] = int(input("How much do you bid?\n$"))

        more_bidders = input('Is anyone else bidding? Type "yes" or "no".\n').lower()
        if more_bidders != "yes":
            bidding = False
        os.system("cls")

    winner = max(bids, key=bids.get)
    print(f"The winner is {winner} with a bid of ${bids[winner]}!")


if __name__ == "__main__":
    secret_auction()
