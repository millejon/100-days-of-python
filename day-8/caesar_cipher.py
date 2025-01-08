import string

alphabet = list(string.ascii_uppercase) + list(" ")


def encrypt(message: str, shift: int) -> str:
    """Encrypt message using Caesar cipher.

    Arguments:
        message -- Message to encrypt
        shift -- Number of positions to rotate the plain alphabet

    Returns:
        Encrypted message
    """
    message = list(message)

    for index, letter in enumerate(message):
        letter = letter.upper()
        if letter in alphabet:
            encrypted_letter_index = (alphabet.index(letter) + shift) % len(alphabet)
            message[index] = alphabet[encrypted_letter_index]

    return "".join(message)


if __name__ == "__main__":
    mode = input(
        'Enter "encode" to encrypt or "decode" to decrypt your message:\n'
    ).lower()
    message = input("Enter your message:\n")
    shift = int(input("Enter the shift:\n"))
    print(f"This is your encrypted message: {encrypt(message, shift)}")
