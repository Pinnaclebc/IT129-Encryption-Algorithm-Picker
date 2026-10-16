# Developed by: Shawn Will O. Velasco

import string

KEY = "qwertyuiopasdfghjklzxcvbnm"


def encrypt(text, key):
    table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                          key.lower() + key.upper())
    return text.translate(table)


def decrypt(text, key):
    table = str.maketrans(key.lower() + key.upper(),
                          string.ascii_lowercase + string.ascii_uppercase)
    return text.translate(table)


def MonoalphabeticEncrypt() -> None:
    """Ask for a message, then show the encrypted and decrypted result."""
    print(" ")
    message = input("Enter message: ")
    cipher = encrypt(message, KEY)

    print("Encrypted:", cipher)
    print("Decrypted:", decrypt(cipher, KEY))