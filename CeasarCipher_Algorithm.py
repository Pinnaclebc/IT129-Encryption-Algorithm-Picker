# Developed by: Davy Carl V. Sambile

def caesarCipher(text, shift, mode):
    result = ""

    # Use a negative shift for decryption
    if mode == "Decrypt":
        shift = -shift

    print(f"\n{mode}ing letter by letter:")
    print("-" * 65)
    print(f"{'#':<4} {'Char':<8} {'Position':<12} {'Shift':<10} {'New Position':<16} {'Output'}")
    print("-" * 65)

    for i, char in enumerate(text):
        if char.isalpha():
            # Keep uppercase and lowercase letters
            base = ord('a') if char.islower() else ord('A')

            # Get the letter's position (A = 1 to Z = 26)
            position = ord(char) - base + 1

            # Shift the letter and wrap around the alphabet
            newPosition = (position - 1 + shift) % 26 + 1

            # Convert the new position back into a letter
            outputChar = chr(newPosition - 1 + base)

            print(
                f"{i + 1:<4} {repr(char):<8} {position:<12} "
                f"{shift:<10} {newPosition:<16} {repr(outputChar)}"
            )

            result += outputChar

        else:
            # Keep spaces, numbers, and punctuation unchanged
            print(
                f"{i + 1:<4} {repr(char):<8} {'-':<12} "
                f"{'-':<10} {'-':<16} {repr(char)}"
            )
            result += char

    print("-" * 65)
    return result

def CeasarEncrypt():
    print("\n=== Caesar Cipher Tool ===")

    text = input("Enter the string to encrypt: ")

    if not text:
        print("Error: The string cannot be empty.")
        return

    try:
        shift = int(input("Enter the shift value (1-25): "))
        if not 1 <= shift <= 25:
            print("Error: The shift value must be between 1 and 25.")
            return
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    # Encrypt the text
    encryptedText = caesarCipher(text, shift, "Encrypt")
    print(f"\nEncrypted string: {encryptedText}")

    # Ask whether to decrypt or exit
    while True:
        choice = input(
            "\nWhat would you like to do? [D]ecrypt or [E]xit: "
        ).strip().lower()

        if choice in ("d", "decrypt"):
            decryptedText = caesarCipher(
                encryptedText, shift, "Decrypt"
            )
            print(f"\nRecovered Plaintext: {decryptedText}")
            break

        elif choice in ("e", "exit"):
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please type D or E.")

if __name__ == "__main__":
    CeasarEncrypt()