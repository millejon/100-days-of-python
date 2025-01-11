def band_name_generator() -> None:
    """Generate a band name."""
    print("Welcome to the band name generator!")

    city = input("What city did you grow up in?\n")
    pet = input("What is your pet's name?\n")

    print(f"Your band name could be {city} {pet}!")


if __name__ == "__main__":
    band_name_generator()
