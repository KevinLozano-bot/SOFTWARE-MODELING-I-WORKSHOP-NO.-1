"""Command Line Interface for the Arcade Machine Catalog System."""

import sys
from typing import List, Optional

# Assume the previous code is in a file named arcade_catalog.py
from arcade_catalog import MachineFactory, CatalogManager, Machine, Videogame

def print_menu():
    """Print the main menu options for the Arcade Machine Catalog CLI."""
    print("\nArcade Machine Catalog Menu:")
    print("1. Create a new machine")
    print("2. Add a videogame to a machine")
    print("3. Search machines")
    print("4. List all machines")
    print("5. Exit")

def create_machine(factory: MachineFactory, catalog: CatalogManager):
    """Create a new machine and add it to the catalog.

    This function prompts the user to select a machine type, material, and color,
    then creates the machine using the factory and adds it to the catalog.

    Args:
        factory: The MachineFactory object used to create machines.
        catalog: The CatalogManager object used to store machines.
    """
    machine_types = ["DanceRevolution", "ClassicalArcade", "Shooting", "Racing", "VirtualReality"]
    materials = ["wood", "aluminium", "carbon fiber"]

    print("\nAvailable machine types:")
    for i, m_type in enumerate(machine_types, 1):
        print(f"{i}. {m_type}")

    type_choice = int(input("Select machine type (1-5): ")) - 1
    if type_choice < 0 or type_choice >= len(machine_types):
        print("Invalid choice.")
        return

    print("\nAvailable materials:")
    for i, material in enumerate(materials, 1):
        print(f"{i}. {material}")

    material_choice = int(input("Select material (1-3): ")) - 1
    if material_choice < 0 or material_choice >= len(materials):
        print("Invalid choice.")
        return

    color = input("Enter color: ")

    machine = factory.create_machine(machine_types[type_choice], materials[material_choice], color)
    if machine:
        catalog.register_machine(machine)
        print(f"Created {machine_types[type_choice]} machine with {materials[material_choice]} material and {color} color.")
    else:
        print("Failed to create machine.")

def add_videogame(catalog: CatalogManager):
    """Add a videogame to an existing machine in the catalog.

    This function prompts the user to select a machine from the catalog,
    then enter details for a new videogame to add to that machine.

    Args:
        catalog: The CatalogManager object containing the machines.
    """
    if not catalog.machines:
        print("No machines available. Create a machine first.")
        return

    print("\nAvailable machines:")
    for i, machine in enumerate(catalog.machines, 1):
        print(f"{i}. {type(machine).__name__} ({machine.color})")

    choice = int(input("Select a machine to add a videogame (1-{}): ".format(len(catalog.machines)))) - 1
    if choice < 0 or choice >= len(catalog.machines):
        print("Invalid choice.")
        return

    machine = catalog.machines[choice]

    name = input("Enter videogame name: ")
    storytelling_creator = input("Enter storytelling creator: ")
    graphics_creator = input("Enter graphics creator: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    year = int(input("Enter year: "))
    is_hd = input("Is it high definition? (y/n): ").lower() == 'y'

    game = Videogame(name, storytelling_creator, graphics_creator, category, price, year, is_hd)
    machine.add_videogame(game)
    print(f"Added {game.name} to the selected machine.")

def search_machines(catalog: CatalogManager):
    """Search for machines in the catalog based on various criteria.

    This function prompts the user to select a search option and enter
    the corresponding search parameters, then displays the matching machines.

    Args:
        catalog: The CatalogManager object containing the machines to search.
    """
    print("\nSearch options:")
    print("1. By videogame count")
    print("2. By material")
    print("3. By videogame name")
    print("4. By price range")
    print("5. By weight range")
    print("6. By power consumption range")

    choice = int(input("Select search option (1-6): "))

    if choice == 1:
        count = int(input("Enter videogame count: "))
        results = catalog.search_by_videogame_count(count)
    elif choice == 2:
        material = input("Enter material: ")
        results = catalog.search_by_material(material)
    elif choice == 3:
        name = input("Enter videogame name: ")
        results = catalog.search_by_videogame_name(name)
    elif choice == 4:
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        results = catalog.search_by_price_range(min_price, max_price)
    elif choice == 5:
        min_weight = float(input("Enter minimum weight: "))
        max_weight = float(input("Enter maximum weight: "))
        results = catalog.search_by_weight_range(min_weight, max_weight)
    elif choice == 6:
        min_power = float(input("Enter minimum power consumption: "))
        max_power = float(input("Enter maximum power consumption: "))
        results = catalog.search_by_power_consumption_range(min_power, max_power)
    else:
        print("Invalid choice.")
        return

    if results:
        print("\nSearch results:")
        for i, machine in enumerate(results, 1):
            print(f"{i}. {type(machine).__name__} ({machine.color}) - Price: ${machine.calculate_total_price():.2f}")
    else:
        print("No machines found matching the search criteria.")

def list_all_machines(catalog: CatalogManager):
    """List all machines currently in the catalog.

    This function displays a numbered list of all machines in the catalog,
    showing the machine type, color, and total price.

    Args:
        catalog: The CatalogManager object containing the machines to list.
    """
    if not catalog.machines:
        print("No machines in the catalog.")
        return

    print("\nAll machines in the catalog:")
    for i, machine in enumerate(catalog.machines, 1):
        print(f"{i}. {type(machine).__name__} ({machine.color}) - Price: ${machine.calculate_total_price():.2f}")

def main():
    """Main function to run the Arcade Machine Catalog CLI.

    This function initializes the MachineFactory and CatalogManager,
    then enters a loop to display the menu and process user input until
    the user chooses to exit.
    """
    factory = MachineFactory()
    catalog = CatalogManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_machine(factory, catalog)
        elif choice == '2':
            add_videogame(catalog)
        elif choice == '3':
            search_machines(catalog)
        elif choice == '4':
            list_all_machines(catalog)
        elif choice == '5':
            print("Thank you for using the Arcade Machine Catalog. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()