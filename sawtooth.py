import os
import sys
import webbrowser
# Developed by Bruce M. Canga

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
    file_name = "sawtooth.jpg"
    if os.path.exists(file_name):
        file_path = os.path.abspath(file_name)
        link = "file:///" + file_path.replace("\\", "/")
        print("Click this link to view the art:")
        print(link)
        webbrowser.open(link)
    else:
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
        elif user_input.isalpha() == False:
            print("Please enter letters only. No numbers or special characters allowed.")
        else:
            return user_input

def encode_msg():
    plain_text = get_valid_input("Enter plain text: ")
    print("Key space: letters A-Z only, any length (spaces are ignored).")
    keyword = get_valid_input("Enter keyword: ")
    
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
    
    print("\nShoe Layout:")
    half_length = int(len(shifted) / 2)
    left_col = shifted[0:half_length]
    right_col = shifted[half_length:len(shifted)]
    
    for i in range(half_length):
        print("Left: " + left_col[i] + "      Right: " + right_col[i])
    if pause_step() == False:
        return
    
    print("\nStep 3: Left Lace Path straight across")
    print("Explanation: The left lace goes straight horizontally from the left side to the right side.")
    
    left_path = ""
    for i in range(half_length):
        left_path = left_path + left_col[i] + right_col[i]
        
    path_visual = ""
    for char in left_path:
        path_visual = path_visual + char + " => "
    print("Left Path: " + path_visual.strip(" => "))
    if pause_step() == False:
        return
    
    print("\nStep 4: Right Lace Path diagonal then straight")
    print("Explanation: The right lace crosses diagonally down to the left then goes straight to the right.")
    
    right_path = ""
    for i in range(half_length):
        if i == 0:
            right_path = right_path + right_col[i]
        else:
            right_path = right_path + left_col[i] + right_col[i]
            
    path_visual2 = ""
    for char in right_path:
        path_visual2 = path_visual2 + char + " => "
    print("Right Path: " + path_visual2.strip(" => "))
    if pause_step() == False:
        return
    
    print("\nStep 5: Combine paths for final cipher")
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

    # A valid Sawtooth ciphertext is a left path of n letters plus a right path of n - 1 letters,
    # where n is always even (the shoe has two columns). So the length is always 3, 7, 11, 15, ...
    if len(cipher_text) % 4 != 3:
        print("\nError: A Sawtooth ciphertext length must be 3, 7, 11, 15... (one less than a multiple of 4).")
        print("You entered " + str(len(cipher_text)) + " letters. Check that you copied the whole message.")
        return
        
    print("\nStep 1: Calculate shoe size and split paths")
    print("Explanation: We find the original length by dividing the cipher text and splitting it into the Left and Right laces.")
    left_length = int((len(cipher_text) + 1) / 2)
    left_path = cipher_text[0:left_length]
    right_path = cipher_text[left_length:len(cipher_text)]
    print("Left Path extracted:  " + left_path)
    print("Right Path extracted: " + right_path)
    if pause_step() == False:
        return
    
    print("\nStep 2: Verify the Right Lace pattern")
    print("Explanation: We check if the diagonal right path matches the straight left path to ensure no data was lost.")
    expected_right = left_path[1:len(left_path)]
    if expected_right == right_path:
        print("Right path verified. No data corruption.")
    else:
        print("Warning: Data might be corrupted.")
    if pause_step() == False:
        return
    
    print("\nStep 3: Rebuild Shifted Word")
    print("Explanation: The Left path contains the letters read horizontally across the shoe. We must untangle them back into their original left and right columns.")
    
    left_col = ""
    right_col = ""
    for i in range(len(left_path)):
        if i % 2 == 0:
            left_col = left_col + left_path[i]
        else:
            right_col = right_col + left_path[i]
            
    print("\nRebuilt Shoe Layout:")
    for i in range(len(left_col)):
        print("Left: " + left_col[i] + "      Right: " + right_col[i])
        
    shifted = left_col + right_col
    print("\nShifted word combined: " + shifted)
    if pause_step() == False:
        return
    
    print("\nStep 4: Reverse the Keyword Shift")
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
    while True:
        print("\n" + "=" * 46)
        print("           SAWTOOTH LACE ALGORITHM")
        print("=" * 46)
        show_art()
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