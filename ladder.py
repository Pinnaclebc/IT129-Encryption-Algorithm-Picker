import os
import sys
import webbrowser

def pause_step():
    choice = input("\nProceed to next step y/n: ")
    if choice.lower() == 'n':
        print("Going back to menu...")
        return False
    return True

def show_art():

    file_name = "ladder.jpg"
    if os.path.exists(file_name):
        file_path = os.path.abspath(file_name)
        link = "file:///" + file_path.replace("\\", "/")
        print("\nClick this link to view the art:")
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
    
    print("\nStep 3: Blue Lace Path Weave")
    print("Explanation: The blue lace alternates directions every row going Left to Right then Right to Left.")
    blue_path = ""
    for i in range(half_length):
        if i % 2 == 0:
            blue_path = blue_path + left_col[i] + right_col[i]
        else:
            blue_path = blue_path + right_col[i] + left_col[i]
            
    path_visual = ""
    for i in range(0, len(blue_path), 2):
        path_visual = path_visual + blue_path[i:i+2] + " => "
    print("Blue Path: " + path_visual.strip(" => "))
    if pause_step() == False:
        return
    
    print("\nStep 4: Red Lace Path Lock")
    print("Explanation: The red lace perfectly mirrors the blue lace to lock the weave securely.")
    red_path = ""
    for i in range(half_length):
        if i % 2 == 0:
            red_path = red_path + right_col[i] + left_col[i]
        else:
            red_path = red_path + left_col[i] + right_col[i]
            
    path_visual2 = ""
    for i in range(0, len(red_path), 2):
        path_visual2 = path_visual2 + red_path[i:i+2] + " => "
    print("Red Path: " + path_visual2.strip(" => "))
    if pause_step() == False:
        return
    
    print("\nStep 5: Combine paths for final cipher")
    print("Explanation: We attach the Red Path to the end of the Blue Path making the final message twice as long.")
    final_cipher = blue_path + red_path
    print("Encrypted message: " + final_cipher)
    if pause_step() == False:
        return
        
    print("\nDo you want to decode this exact message right now to see the process? y/n")
    auto_choice = input("Choice: ").lower()
    if auto_choice == 'y':
        decode_msg(final_cipher, keyword)

def decode_msg(auto_cipher="", auto_key=""):
    if auto_cipher == "":
        cipher_text = get_valid_input("Enter encrypted text: ")
    else:
        cipher_text = auto_cipher
        print("\nAuto loading encrypted text: " + cipher_text)
        
    if auto_key == "":
        keyword = get_valid_input("Enter keyword: ")
    else:
        keyword = auto_key
        print("Auto loading keyword: " + keyword)
        
    print("\nStep 1: Split paths")
    print("Explanation: The encrypted message is cut perfectly in half to separate the Blue and Red laces.")
    half_point = int(len(cipher_text) / 2)
    blue_path = cipher_text[0:half_point]
    red_path = cipher_text[half_point:len(cipher_text)]
    print("Blue Path extracted:  " + blue_path)
    print("Red Path extracted: " + red_path)
    if pause_step() == False:
        return
    
    print("\nStep 2: Verify the Ladder Locks")
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
        print("Warning: Data might be corrupted. Locks do not match.")
    if pause_step() == False:
        return
    
    print("\nStep 3: Untangle the Weave and Rebuild Shoe Layout")
    print("Explanation: We take the Blue path and place the letters back into the left and right columns alternating directions.")
    
    left_col = ""
    right_col = ""
    pair_index = 0
    for i in range(0, len(blue_path), 2):
        pair = blue_path[i:i+2]
        if pair_index % 2 == 0:
            left_col = left_col + pair[0]
            right_col = right_col + pair[1]
        else:
            left_col = left_col + pair[1]
            right_col = right_col + pair[0]
        pair_index = pair_index + 1
        
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
        print("            LADDER LACE ALGORITHM")
        print("=" * 46)
        show_art()
        print("\n1. Encode Message")
        print("2. Decode Message")
        print("3. Go back to Lace Menu")
        print("4. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            encode_msg()
        elif choice == '2':
            decode_msg()
        elif choice == '3':
            os.system("python lace_algos.py")
            return
        elif choice == '4':
            sys.exit(1)
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main_menu()