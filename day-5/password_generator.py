import random
import string

LETTERS = list(string.ascii_letters)
NUMBERS = list(string.digits)
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def compose_password(letters: int = 0, numbers: int = 0, symbols: int = 0) -> str:
    """Compose a random password of letters, numbers, and symbols.

    Arguments:
        letters -- The amount of letters to include
        numbers -- The amount of numbers to include
        symbols -- The amount of symbols to include

    Returns:
        Randomly generated password
    """
    random.seed()
    password = []

    for _ in range(letters):
        password.append(random.choice(LETTERS))
    for _ in range(numbers):
        password.append(random.choice(NUMBERS))
    for _ in range(symbols):
        password.append(random.choice(SYMBOLS))

    random.shuffle(password)
    return "".join(password)


def password_generator() -> None:
    """Generate a random password."""
    print("Welcome to the password generator!")

    letters = int(input("How many letters would you like in your password?\n"))
    numbers = int(input("How many numbers would you like?\n"))
    symbols = int(input("How many symbols would you like?\n"))

    print(f"Your password is {compose_password(letters, numbers, symbols)}")


if __name__ == "__main__":
    password_generator()
