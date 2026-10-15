"""Console menu for selecting placeholder encryption algorithms."""

import placeholder_algorithm_1
import placeholder_algorithm_2
import lace_algos
import os
import sys
import CeasarCipher_Algorithm


MENU_OPTIONS = {
    "1": "Placeholder Algorithm 1",
    "2": "Placeholder Algorithm 2",
    "3": "Ceasar Cipher Algorithm",
    "4": "Lace Algorithms",
    "5": "Exit",
}


def display_menu() -> None:
    """Display the available encryption algorithm choices."""
    print("\n" + "=" * 46)
    print("           ENCRYPTION ALGORITHM PICKER")
    print("=" * 46)
    for number, option_name in MENU_OPTIONS.items():
        print(f"  [{number}] {option_name}")
    print("=" * 46)


def run_menu() -> None:
    """Keep displaying the menu until the user chooses to exit."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice not in MENU_OPTIONS:
            print("\nInvalid input. Please enter a number from 1 to 5.")
            continue

        if choice == "5":
            print("\nExiting Encryption Algorithm Picker. Goodbye!")
            break
        
        if choice == "4":
            exit_code = os.system("python lace_algos.py")
            if exit_code != 0:
                sys.exit()

        print(f"\nYou selected: {MENU_OPTIONS[choice]}")

        if choice == "1":
            placeholder_algorithm_1.placeholder_algorithm_1()
        elif choice == "2":
            placeholder_algorithm_2.placeholder_algorithm_2()
        elif choice == "3": 
            CeasarCipher_Algorithm.CeasarEncrypt()
        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    run_menu()
