# Developed by: Shawn Will O. Velasco

import string


def getKey() -> str:
    """Ask the user for a valid 26-letter key."""
    while True:
        key = input("Enter 26-letter key (each letter once): ").strip().lower()

        if len(key) != 26 or set(key) != set(string.ascii_lowercase):
            print("Invalid key. It must contain all 26 letters exactly once.\n")
            continue

        return key


def monoalphabeticCipher(text, key, mode):
    result = ""

    # Create the substitution table
    if mode == "Decrypt":
        source = key.lower() + key.upper()
        target = string.ascii_lowercase + string.ascii_uppercase
    else:
        source = string.ascii_lowercase + string.ascii_uppercase
        target = key.lower() + key.upper()

    table = str.maketrans(source, target)

    print(f"\n{mode}ing letter by letter:")
    print("-" * 75)
    print(
        f"{'#':<4} {'Char':<8} {'Position':<12} "
        f"{'Key Char':<12} {'Output':<10}"
    )
    print("-" * 75)

    for i, char in enumerate(text):
        if char.isalpha() and char.lower() in string.ascii_lowercase:

            if mode == "Decrypt":
                # Position of the cipher letter inside the key
                position = key.index(char.lower()) + 1
                keyChar = char
            else:
                # Position of the plain letter in the alphabet (A = 1 to Z = 26)
                position = ord(char.lower()) - ord('a') + 1
                keyChar = key[position - 1]
                if char.isupper():
                    keyChar = keyChar.upper()

            outputChar = char.translate(table)

            print(
                f"{i + 1:<4} {repr(char):<8} {position:<12} "
                f"{repr(keyChar):<12} {repr(outputChar):<10}"
            )

            result += outputChar

        else:
            # Keep spaces, numbers, and punctuation unchanged
            print(
                f"{i + 1:<4} {repr(char):<8} {'-':<12} "
                f"{'-':<12} {repr(char):<10}"
            )
            result += char

    print("-" * 75)
    return result


def MonoalphabeticEncrypt() -> None:
    """Ask for a key and message, then show encryption and decryption steps."""

    print("\n=== Monoalphabetic Cipher Tool ===")

    key = getKey()

    message = input("Enter message to encrypt: ")

    if not message:
        print("Error: The message cannot be empty.")
        return

    # Encrypt the message
    encryptedText = monoalphabeticCipher(message, key, "Encrypt")
    print(f"\nEncrypted string: {encryptedText}")

    # Ask whether to decrypt or exit
    while True:
        choice = input(
            "\nWhat would you like to do? [D]ecrypt or [E]xit: "
        ).strip().lower()

        if choice in ("d", "decrypt"):
            decryptedText = monoalphabeticCipher(encryptedText, key, "Decrypt")
            print(f"\nRecovered Plaintext: {decryptedText}")
            break

        elif choice in ("e", "exit"):
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please type D or E.")


if __name__ == "__main__":
    MonoalphabeticEncrypt()