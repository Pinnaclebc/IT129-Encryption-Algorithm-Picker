import sys
import ladder
import sawtooth
import Lace_combined

# Developed by: Bruce M. Canga

def main_menu():
    while True:
        print("\n" + "=" * 46)
        print("           ENCRYPTION ALGORITHM PICKER")
        print("=" * 46)
        print("A - Sawtooth lace")
        print("B - Ladder lace")
        print("C - Ladder + Sawtooth lace (combined)")
        print("D - Go back to the Main Menu")
        print("E - Exit program")
        
        choice = input("\nChoose an option A B C D or E: ").upper().strip()
        
        if choice == 'A':
            sawtooth.main_menu()
        elif choice == 'B':
            ladder.main_menu()
        elif choice == 'C':
            Lace_combined.main_menu()
        elif choice == 'D':
            # break ends this menu loop and returns to the main menu that called it
            break
        elif choice == 'E':
            print("\nExiting program.")
            sys.exit()
        else:
            print("\nInvalid choice bro. Please enter exactly A B C D or E.")

if __name__ == '__main__':
    main_menu()