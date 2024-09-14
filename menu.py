"""
Main menu module for the Game Console CLI.

This module contains the necessary functions to display an interactive menu and manage user selections for a Game Console.
and manage user selections for a Game Console.

AUTHOR: Kevin Estiven Lozano Duarte <kelozanod@udistrital.edu.co>

This file is part of WORKSHOPNo1.

WORKSHOPNo1 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

WORKSHOPNo1 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with WORKSHOPNo1. If not, see <https://www.gnu.org/licenses/>.

"""
import sys
from console_functions import AdvancedGamingConsole  # Use the concrete class

class InvalidChoiceError(Exception):
    """Exception raised for invalid choices in the menu."""
    pass

def display_menu():
    """
    Displays the main menu of the Game Console CLI.

    Provides a list of options for the user to choose from.
    """
    print("\nUser Menu for advice to buy your video game machine :")
    print("1. Display specifications")
    print("2. Storage options")
    print("3. Compatibility information")
    print("4. Compare with other consoles")
    print("5. Customization options")
    print("6. Durability information")
    print("7. Demo and testing")
    print("8. Accessibility features")
    print("9. AI technologies")
    print("10. Audio options")
    print("11. Power consumption")
    print("12. Security options")
    print("13. Ray-tracing performance")
    print("14. Network configuration")
    print("15. Sales guidance")
    print("0. Exit")

def get_valid_choice():
    """
    Request and validates the user's choice.

    Returns:
        int: The user's valid choice (0-15).

    Raises:
        InvalidChoiceError: If the choice is outside the valid range.
    """
    while True:
        try:
            choice = input("Enter your choice (0-15): ")
            choice = int(choice)
            if 0 <= choice <= 15:
                return choice
            else:
                raise InvalidChoiceError("Choice must be between 0 and 15.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
        except InvalidChoiceError as e:
            print(f"Error: {e}")

def execute_choice(console, choice):
    """
    Executes the function corresponding to the user's choice.

    Args:
        console (AdvancedGamingConsole): Instance of the AdvancedGamingConsole class.
        choice (int): The user's choice.

    Raises:
        InvalidChoiceError: If the choice does not correspond to any function.
        AttributeError: If the selected function is not implemented.
    """
    actions = {
        1: console.display_specs,
        2: console.storage_options,
        3: console.show_compatibility,
        4: console.compare,
        5: console.customization,
        6: console.durability,
        7: console.demo_info,
        8: console.accessibility,
        9: console.ai_technologies,
        10: console.audio_options,
        11: console.power_consumption,
        12: console.security,
        13: console.ray_tracing_performance,
        14: console.network_config,
        15: console.sales_guidance,
        0: lambda: sys.exit("Thank you for using the User Menu for advice to buy your video game machine . Goodbye!")
    }
    
    try:
        print(f"Executing choice: {choice}")  # Debugging line
        action = actions.get(choice)
        if action:
            action()
        else:
            raise InvalidChoiceError("Invalid choice.")
    except InvalidChoiceError as e:
        print(f"Error: {e}")
    except AttributeError as e:
        print(f"Error: The selected function is not available. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function that executes the CLI menu loop.

    Initializes the console instance and continuously displays the menu
    until the user decides to exit.
    """
    console = AdvancedGamingConsole()  # Use the concrete class
    
    while True:
        display_menu()
        choice = get_valid_choice()
        execute_choice(console, choice)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
