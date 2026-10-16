# Developed by: Shawn Will O. Velasco

import string

KEY = "qwertyuiopasdfghjklzxcvbnm"

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

            # Get the letter's position (A = 1 to Z = 26)
            position = ord(char.lower()) - ord('a') + 1

            # Get the corresponding substituted character
            outputChar = char.translate(table)

            # Get the corresponding character in the substitution key
            keyChar = key[position - 1]

            # Preserve the original letter's case
            if char.isupper():
                outputChar = outputChar.upper()
                keyChar = keyChar.upper()

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
    """Ask for a message, then show encryption and decryption steps."""

    print("\n=== Monoalphabetic Cipher Tool ===")

    message = input("Enter message to encrypt: ")

    if not message:
        print("Error: The message cannot be empty.")
        return

    # Encrypt the message
    encryptedText = monoalphabeticCipher(message, KEY, "Encrypt")
    print(f"\nEncrypted string: {encryptedText}")

    # Ask whether to decrypt or exit
    while True:
        choice = input(
            "\nWhat would you like to do? [D]ecrypt or [E]xit: "
        ).strip().lower()

        if choice in ("d", "decrypt"):

            # Decrypt the encrypted message
            decryptedText = monoalphabeticCipher(
                encryptedText, KEY, "Decrypt"
            )
            print(f"\nRecovered Plaintext: {decryptedText}")
            break

        elif choice in ("e", "exit"):
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please type D or E.")

if __name__ == "__main__":
    MonoalphabeticEncrypt()