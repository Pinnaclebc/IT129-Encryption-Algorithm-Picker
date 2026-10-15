def xor_char(char, key_char):
    """XOR a single character with a single key character."""
    return chr(ord(char) ^ ord(key_char))


# Self made
def xor_cipher(text, key):

    # Storage for the values
    result = []

    # Encryption
    for i, char in enumerate(text):

        # Key repeats through modulo if key is shorter than plaintext.
        key_char = key[i % len(key)]
        result.append(xor_char(char, key_char))

    # Returns the values stored in the array
    return "".join(result)


def show_steps(text, key, mode):
    """Prints the letter-by-letter breakdown and returns the result."""
    print(f"\n{mode}ing letter by letter:")
    print("-" * 78)
    print(f"{'#':<3} {'Char':<6} {'Binary':<10} {'Key':<6} {'Binary':<10} "
          f"{'XOR Result':<10} {'Output'}")
    print("-" * 78)

    for i, char in enumerate(text):
        key_char = key[i % len(key)]
        out_char = xor_char(char, key_char)
        print(f"{i + 1:<3} {repr(char):<6} {ord(char):08b}   "
              f"{repr(key_char):<6} {ord(key_char):08b}   "
              f"{ord(char) ^ ord(key_char):08b}   {repr(out_char)}")

    print("-" * 78)
    return xor_cipher(text, key)


def main():

    print("=== Bitwise XOR Cipher Tool ===")

    plaintext = input("Enter the plaintext to encrypt: ")
    key = input("Enter the secret key: ")

    if not plaintext:
        print("Error: The plaintext cannot be empty.")
        return
    if not key:
        print("Error: The key cannot be empty.")
        return

    # Encrypt with step-by-step display
    encrypted_text = show_steps(plaintext, key, "Encrypt")
    print(f"\nCiphertext (raw): {repr(encrypted_text)}")
    print(f"Ciphertext (hex): {' '.join(f'{ord(c):02x}' for c in encrypted_text)}")

    # Ask the user what to do next
    while True:
        choice = input("\nWhat would you like to do? "
                       "[D]ecrypt or [E]xit: ").strip().lower()

        if choice in ("d", "decrypt"):
            decrypted_text = show_steps(encrypted_text, key, "Decrypt")
            print(f"\nRecovered Plaintext: {decrypted_text}")
            break
        elif choice in ("e", "exit"):
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please type D to decrypt or E to exit.")


if __name__ == "__main__":
    main()