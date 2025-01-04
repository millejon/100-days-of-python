import random
import string

LETTERS = list(string.ascii_letters)
NUMBERS = list(string.digits)
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate_password(letters: int = 0, numbers: int = 0, symbols: int = 0) -> str:
    """Return random combination of letters, numbers, and symbols.

    Arguments:
        letters -- Amount of letters to include in password
        numbers -- Amount of numbers to include in password
        symbols -- Amount of symbols to include in password

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


if __name__ == "__main__":
    print("Welcome to the password generator!")
    letters = int(input("How many letters would you like in your password?\n"))
    numbers = int(input("How many numbers would you like?\n"))
    symbols = int(input("How many symbols would you like?\n"))
    print(f"Your password is {generate_password(letters, numbers, symbols)}")
