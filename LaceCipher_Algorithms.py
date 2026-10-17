import os 
import sys
import webbrowser
import ladder
import sawtooth

# Developed by: Bruce M. Canga

def show_art():
    
    file_name = "algo_pic.jpg"
    
    if os.path.exists(file_name):
        file_path = os.path.abspath(file_name)
        link = "file:///" + file_path.replace("\\", "/")
        
        print("Click this link to view the art:")
        print(link)
        
        webbrowser.open(link)
    else:
        print("The picture file is missing from the folder.")

def main_menu():
    show_art()
    
    while True:
        print("\n" + "=" * 46)
        print("           ENCRYPTION ALGORITHM PICKER")
        print("=" * 46)
        print("A - Sawtooth lace")
        print("B - Ladder lace")
        print("C - Go back to the Main Menu")
        print("D - Exit program")
        
        choice = input("\nChoose an option A B C or D: ").upper().strip()
        
        if choice == 'A':
            sawtooth.main_menu()
        elif choice == 'B':
            ladder.main_menu()
        elif choice == 'C':
            break
        elif choice == 'D':
            print("\nExiting program.")
            sys.exit()
        else:
            print("\nInvalid choice bro. Please enter exactly A B C or D.")

if __name__ == '__main__':
    main_menu()