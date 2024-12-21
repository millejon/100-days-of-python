def generate_band_name() -> str:
    """Return band name generated from user input."""
    city = input("What city did you grow up in?\n")
    pet = input("What is your pet's name?\n")

    return f"{city} {pet}"


if __name__ == "__main__":
    print("Welcome to the band name generator!")
    print(f"Your band name could be {generate_band_name()}!")
