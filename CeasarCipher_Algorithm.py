# This is a Caesar Cipher Algorithm
# Developed by: Davy Carl V. Sambile

def CeasarEncrypt():
    encryptedString = ""

    print(" ")
    stringInput = input("Enter the string to encrypt: ")
    shiftInput = int(input("Enter the shift value (1-25): "))

    for char in stringInput:
        if char.isalpha():
            shift = shiftInput % 26

            if char.islower():
                encryptedChar = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encryptedChar = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            encryptedString += encryptedChar
        else:
            encryptedString += char

    print(f"Encrypted string: {encryptedString}")