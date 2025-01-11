import string

import ascii_art as art

ALPHABET = list(string.ascii_uppercase) + list(" ")


def translate(message: str, shift: int, mode: str) -> str:
    """Translate a message with the Caesar cipher.

    Arguments:
        message -- The message to translate
        shift -- The number of positions to rotate the plain alphabet
        mode -- "encode" to encrypt, "decode" to decrypt

    Returns:
        Translated message
    """
    message = list(message.upper())
    if mode == "decode":
        shift *= -1

    for index, letter in enumerate(message):
        if letter in ALPHABET:
            shifted_index = (ALPHABET.index(letter) + shift) % len(ALPHABET)
            message[index] = ALPHABET[shifted_index]

    return "".join(message)


def caesar_cipher() -> None:
    """Encrypt or decrypt messages using the Caesar cipher."""
    print(art.logo)
    print("Welcome to the Caesar cipher!")
    translating = True

    while translating:
        mode = input(
            'Enter "encode" to encrypt or "decode" to decrypt your message:\n'
        ).lower()
        message = input("Enter your message:\n")
        shift = int(input("Enter the shift:\n"))

        print(f"This is your {mode}d message: {translate(message, shift, mode)}")
        rerun = input(
            'Type "yes" if you want to translate another message, type "no" to quit.\n'
        ).lower()
        if rerun != "yes":
            translating = False
            print("Thank you for using the Caesar cipher!")


if __name__ == "__main__":
    caesar_cipher()
