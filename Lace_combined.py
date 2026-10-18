import os
import sys
import webbrowser

# Developed by Bruce M. Canga
# Ladder-Sawtooth Lace: ONE cipher that passes the message through the Ladder lace
# first and then through the Sawtooth lace. Decode undoes Sawtooth first, then Ladder.

# The picture that opens in the menu. The first file found in the folder is used.
ART_FILES = ["algo_pic.jpg", "ladder.jpg", "sawtooth.jpg"]

def pause_step():
    # Keeps asking until the user types exactly y or n
    while True:
        choice = input("\nProceed to next step y/n: ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            print("Going back to menu...")
            return False
        else:
            print("Invalid input. Please type y to continue or n to go back to the menu.")

def ask_yes_no(prompt_text):
    # Same idea as pause_step, but returns True/False without the menu message
    while True:
        choice = input(prompt_text).strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please type y for yes or n for no.")

def show_art():
    for file_name in ART_FILES:
        if os.path.exists(file_name):
            file_path = os.path.abspath(file_name)
            link = "file:///" + file_path.replace("\\", "/")
            print("\nClick this link to view the art:")
            print(link)
            webbrowser.open(link)
            return
    print("The picture file is missing from the folder.")

def get_letter_value(letter):
    try:
        with open("alphabet.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if parts[0] == letter:
                    return int(parts[1])
    except FileNotFoundError:
        print("alphabet.txt is missing.")
    return ord(letter) % 32

def get_valid_input(prompt_text):
    while True:
        user_input = input(prompt_text).upper().replace(" ", "")
        if len(user_input) == 0:
            print("You cannot enter a blank answer. Please try again.")
        elif user_input.isascii() == False or user_input.isalpha() == False:
            print("Please enter letters A-Z only. No numbers, accented letters, or special characters allowed.")
        else:
            return user_input

def row_goes_left_to_right(keyword, row_number):
    # Keyed weave (Ladder layer): the keyword decides the direction of each row.
    # Rows are numbered from 1. The key letter repeats like in the keyword shift.
    # If (key letter value + row number) is even the lace goes Left to Right,
    # if it is odd the lace goes Right to Left.
    key_char = keyword[(row_number - 1) % len(keyword)]
    return (get_letter_value(key_char) + row_number) % 2 == 0

def encode_msg():
    plain_text = get_valid_input("Enter plain text (letters only, spaces are removed): ")
    print("Key space: letters A-Z only, any length (spaces are ignored).")
    keyword = get_valid_input("Enter keyword: ")

    print("\n" + "=" * 12 + " LAYER 1: LADDER " + "=" * 12)

    print("\nStep 1: Pad the word if it has an odd length")
    print("Explanation: The shoe needs an even number of holes to lace properly. We add an X at the end if the plain text is odd.")
    if len(plain_text) % 2 != 0:
        plain_text = plain_text + "X"
        print("Word was odd. Added X at the end.")
    else:
        print("Word is already even. No padding needed.")
    print("Padded text: " + plain_text)
    if pause_step() == False:
        return

    print("\nStep 2: Keyword Shift")
    print("Explanation: We shift each letter of the plain text by adding the value of the keyword letter.")
    shifted = ""
    key_index = 0
    for char in plain_text:
        val_p = get_letter_value(char)
        key_char = keyword[key_index % len(keyword)]
        val_k = get_letter_value(key_char)

        new_val = (val_p + val_k) % 26
        if new_val == 0:
            new_val = 26

        new_char = chr(new_val + 64)
        shifted = shifted + new_char
        print(char + " (" + str(val_p) + ") plus " + key_char + " (" + str(val_k) + ") equals " + new_char + " (" + str(new_val) + ")")
        key_index = key_index + 1

    print("Shifted word: " + shifted)
    if pause_step() == False:
        return

    print("\nLadder Shoe Layout:")
    half_length = int(len(shifted) / 2)
    left_col = shifted[0:half_length]
    right_col = shifted[half_length:len(shifted)]

    for i in range(half_length):
        print("Left: " + left_col[i] + "      Right: " + right_col[i])
    if pause_step() == False:
        return

    print("\nStep 3: Ladder Blue Lace Path Weave")
    print("Explanation: The keyword decides the direction of every row. If the key letter value plus the row number is even, the blue lace goes Left to Right. If it is odd, it goes Right to Left.")
    blue_path = ""
    for i in range(half_length):
        row_number = i + 1
        key_char = keyword[i % len(keyword)]
        val_k = get_letter_value(key_char)
        if row_goes_left_to_right(keyword, row_number):
            direction = "Left to Right"
            blue_path = blue_path + left_col[i] + right_col[i]
        else:
            direction = "Right to Left"
            blue_path = blue_path + right_col[i] + left_col[i]
        print("Row " + str(row_number) + ": " + key_char + " (" + str(val_k) + ") plus row " + str(row_number) + " equals " + str(val_k + row_number) + ", so " + direction)

    path_visual = ""
    for i in range(0, len(blue_path), 2):
        path_visual = path_visual + blue_path[i:i+2] + " => "
    print("Blue Path: " + path_visual.strip(" => "))
    if pause_step() == False:
        return

    print("\nStep 4: Ladder Red Lace Path Lock")
    print("Explanation: The red lace perfectly mirrors the blue lace to lock the weave securely.")
    red_path = ""
    for i in range(half_length):
        if row_goes_left_to_right(keyword, i + 1):
            red_path = red_path + right_col[i] + left_col[i]
        else:
            red_path = red_path + left_col[i] + right_col[i]

    path_visual2 = ""
    for i in range(0, len(red_path), 2):
        path_visual2 = path_visual2 + red_path[i:i+2] + " => "
    print("Red Path: " + path_visual2.strip(" => "))
    if pause_step() == False:
        return

    print("\nStep 5: Combine the Ladder laces")
    print("Explanation: We attach the Red Path to the end of the Blue Path. This is the Ladder result, and it now goes into the Sawtooth lace.")
    ladder_result = blue_path + red_path
    print("Ladder result: " + ladder_result)
    if pause_step() == False:
        return

    print("\n" + "=" * 11 + " LAYER 2: SAWTOOTH " + "=" * 11)

    print("\nStep 6: Sawtooth Shoe Layout")
    print("Explanation: The Ladder result is treated as a brand new word. We split it in half again. The first half goes down the left column and the second half goes down the right column.")
    saw_half = int(len(ladder_result) / 2)
    saw_left = ladder_result[0:saw_half]
    saw_right = ladder_result[saw_half:len(ladder_result)]

    for i in range(saw_half):
        print("Left: " + saw_left[i] + "      Right: " + saw_right[i])
    if pause_step() == False:
        return

    print("\nStep 7: Sawtooth Left Lace Path straight across")
    print("Explanation: The left lace goes straight horizontally from the left side to the right side.")

    left_path = ""
    for i in range(saw_half):
        left_path = left_path + saw_left[i] + saw_right[i]

    path_visual3 = ""
    for char in left_path:
        path_visual3 = path_visual3 + char + " => "
    print("Left Path: " + path_visual3.strip(" => "))
    if pause_step() == False:
        return

    print("\nStep 8: Sawtooth Right Lace Path diagonal then straight")
    print("Explanation: The right lace crosses diagonally down to the left then goes straight to the right.")

    right_path = ""
    for i in range(saw_half):
        if i == 0:
            right_path = right_path + saw_right[i]
        else:
            right_path = right_path + saw_left[i] + saw_right[i]

    path_visual4 = ""
    for char in right_path:
        path_visual4 = path_visual4 + char + " => "
    print("Right Path: " + path_visual4.strip(" => "))
    if pause_step() == False:
        return

    print("\nStep 9: Combine paths for final cipher")
    print("Explanation: We stick the Left Path and the Right Path together to get the completely scrambled message.")
    final_cipher = left_path + right_path
    print("Encrypted message: " + final_cipher)
    if pause_step() == False:
        return

    print("\nDo you want to decode this exact message right now to see the process? y/n")
    if ask_yes_no("Choice: "):
        decode_msg(final_cipher, keyword)

def decode_msg(auto_cipher="", auto_key=""):
    if auto_cipher == "":
        cipher_text = get_valid_input("Enter encrypted text: ")
    else:
        cipher_text = auto_cipher
        print("\nAuto loading encrypted text: " + cipher_text)

    if auto_key == "":
        print("Key space: letters A-Z only, any length (spaces are ignored).")
        keyword = get_valid_input("Enter keyword: ")
    else:
        keyword = auto_key
        print("Auto loading keyword: " + keyword)

    # The Ladder result has 2n letters (n is even), and Sawtooth turns 2n letters into
    # 2n + (2n - 1) = 4n - 1 letters. So a valid length is always 7, 15, 23, 31, ...
    if len(cipher_text) % 8 != 7:
        print("\nError: A Ladder-Sawtooth ciphertext length must be 7, 15, 23, 31... (one less than a multiple of 8).")
        print("You entered " + str(len(cipher_text)) + " letters. Check that you copied the whole message.")
        return

    print("\n" + "=" * 8 + " UNDO LAYER 2: SAWTOOTH " + "=" * 8)

    print("\nStep 1: Calculate shoe size and split the Sawtooth paths")
    print("Explanation: We find the original length by dividing the cipher text and splitting it into the Left and Right laces.")
    left_length = int((len(cipher_text) + 1) / 2)
    left_path = cipher_text[0:left_length]
    right_path = cipher_text[left_length:len(cipher_text)]
    print("Left Path extracted:  " + left_path)
    print("Right Path extracted: " + right_path)
    if pause_step() == False:
        return

    print("\nStep 2: Verify the Sawtooth Right Lace pattern")
    print("Explanation: We check if the diagonal right path matches the straight left path to ensure no data was lost.")
    expected_right = left_path[1:len(left_path)]
    if expected_right == right_path:
        print("Right path verified. No data corruption.")
    else:
        print("Error: The Sawtooth right lace does not match. This is not a valid ciphertext, or it was changed.")
        print("Decoding stopped. Check the ciphertext and try again.")
        return
    if pause_step() == False:
        return

    print("\nStep 3: Untangle the Sawtooth weave to get the Ladder result back")
    print("Explanation: The Left path contains the letters read horizontally across the shoe. We untangle them back into their left and right columns, then join the columns to recover the Ladder result.")

    saw_left = ""
    saw_right = ""
    for i in range(len(left_path)):
        if i % 2 == 0:
            saw_left = saw_left + left_path[i]
        else:
            saw_right = saw_right + left_path[i]

    print("\nRebuilt Sawtooth Shoe Layout:")
    for i in range(len(saw_left)):
        print("Left: " + saw_left[i] + "      Right: " + saw_right[i])

    ladder_result = saw_left + saw_right
    print("\nLadder result recovered: " + ladder_result)
    if pause_step() == False:
        return

    print("\n" + "=" * 9 + " UNDO LAYER 1: LADDER " + "=" * 9)

    print("\nStep 4: Split the Ladder paths")
    print("Explanation: The Ladder result is cut perfectly in half to separate the Blue and Red laces.")
    half_point = int(len(ladder_result) / 2)
    blue_path = ladder_result[0:half_point]
    red_path = ladder_result[half_point:len(ladder_result)]
    print("Blue Path extracted:  " + blue_path)
    print("Red Path extracted: " + red_path)
    if pause_step() == False:
        return

    print("\nStep 5: Verify the Ladder Locks")
    print("Explanation: We check if every two letter pair in the Red path is the exact reverse of the Blue path pair.")
    is_corrupted = False
    for i in range(0, len(blue_path), 2):
        blue_pair = blue_path[i:i+2]
        red_pair = red_path[i:i+2]

        reversed_blue = blue_pair[1] + blue_pair[0]

        if reversed_blue != red_pair:
            is_corrupted = True

    if is_corrupted == False:
        print("Ladder locks verified. No data corruption.")
    else:
        print("Error: The Ladder locks do not match. This is not a valid ciphertext, or it was changed.")
        print("Decoding stopped. Check the ciphertext and try again.")
        return
    if pause_step() == False:
        return

    print("\nStep 6: Untangle the Ladder Weave and Rebuild Shoe Layout")
    print("Explanation: We take the Blue path and use the keyword to find the direction of each row, then place the letters back into the left and right columns.")

    left_col = ""
    right_col = ""
    pair_index = 0
    for i in range(0, len(blue_path), 2):
        pair = blue_path[i:i+2]
        row_number = pair_index + 1
        key_char = keyword[pair_index % len(keyword)]
        val_k = get_letter_value(key_char)
        if row_goes_left_to_right(keyword, row_number):
            direction = "Left to Right"
            left_col = left_col + pair[0]
            right_col = right_col + pair[1]
        else:
            direction = "Right to Left"
            left_col = left_col + pair[1]
            right_col = right_col + pair[0]
        print("Row " + str(row_number) + ": " + key_char + " (" + str(val_k) + ") plus row " + str(row_number) + " equals " + str(val_k + row_number) + ", so " + direction)
        pair_index = pair_index + 1

    print("\nRebuilt Ladder Shoe Layout:")
    for i in range(len(left_col)):
        print("Left: " + left_col[i] + "      Right: " + right_col[i])

    shifted = left_col + right_col
    print("\nShifted word combined: " + shifted)
    if pause_step() == False:
        return

    print("\nStep 7: Reverse the Keyword Shift")
    print("Explanation: We count backwards using the keyword values to reveal the original plain text letters.")
    plain_text = ""
    key_index = 0
    for char in shifted:
        val_c = get_letter_value(char)
        key_char = keyword[key_index % len(keyword)]
        val_k = get_letter_value(key_char)

        for i in range(1, 27):
            if (val_k + i) % 26 == val_c % 26:
                original_char = chr(i + 64)
                plain_text = plain_text + original_char
                print(char + " (" + str(val_c) + ") reversed by " + key_char + " (" + str(val_k) + ") reveals " + original_char + " (" + str(i) + ")")

        key_index = key_index + 1

    print("\nFinal Decoded text: " + plain_text)
    if plain_text.endswith("X"):
        print("Security Note: The final letter is X.")
        print("In cryptography X is often used as a Null to pad odd words.")
        print("Use human context to decide if X is part of the original word or just shoe padding.")
    if pause_step() == False:
        return

def main_menu():
    show_art()
    while True:
        print("\n" + "=" * 46)
        print("       LADDER + SAWTOOTH LACE ALGORITHM")
        print("=" * 46)
        print("\n1. Encode Message")
        print("2. Decode Message")
        print("3. Go back to Lace Menu")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == '1':
            encode_msg()
        elif choice == '2':
            decode_msg()
        elif choice == '3':
            break
        elif choice == '4':
            sys.exit()
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == '__main__':
    main_menu()