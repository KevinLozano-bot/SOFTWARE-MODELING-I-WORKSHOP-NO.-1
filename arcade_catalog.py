"""Arcade Machine Catalog System

This module implements a catalog system for arcade machines, including
various types of machines, videogames, and search functionalities.
"""

import abc
from typing import List, Optional

class Dimensions:
    """Represents the physical dimensions of an arcade machine."""

    def __init__(self, length: float, width: float, height: float):
        """Initialize the Dimensions object.

        Args:
            length: The length of the machine in meters.
            width: The width of the machine in meters.
            height: The height of the machine in meters.
        """
        self.length = length
        self.width = width
        self.height = height

class Videogame:
    """Represents a videogame that can be added to an arcade machine."""

    def __init__(self, name: str, storytelling_creator: str, graphics_creator: str, 
                 category: str, price: float, year: int, is_high_definition: bool):
        """Initialize the Videogame object.

        Args:
            name: The name of the videogame.
            storytelling_creator: The creator of the game's story.
            graphics_creator: The creator of the game's graphics.
            category: The category of the game.
            price: The price of the game.
            year: The year the game was released.
            is_high_definition: Whether the game is in high definition.
        """
        self.name = name
        self.storytelling_creator = storytelling_creator
        self.graphics_creator = graphics_creator
        self.category = category
        self.price = price
        self.year = year
        self.is_high_definition = is_high_definition
        
        if is_high_definition:
            self.price *= 1.1  # 10% increase for HD

class Machine:
    """Represents an arcade machine."""

    def __init__(self, material: str, dimensions: Dimensions, weight: float, 
                 power_consumption: float, memory: int, processors: int, 
                 base_price: float, color: str):
        """Initialize the Machine object.

        Args:
            material: The material the machine is made of.
            dimensions: The physical dimensions of the machine.
            weight: The weight of the machine in kg.
            power_consumption: The power consumption in watts.
            memory: The amount of memory in GB.
            processors: The number of processors.
            base_price: The base price of the machine.
            color: The color of the machine.
        """
        self.material = material
        self.dimensions = dimensions
        self.weight = weight
        self.power_consumption = power_consumption
        self.memory = memory
        self.processors = processors
        self.base_price = base_price
        self.color = color
        self.videogames: List[Videogame] = []

    def add_videogame(self, game: Videogame):
        """Add a videogame to the machine.

        Args:
            game: The Videogame object to add.
        """
        self.videogames.append(game)
        self.base_price += game.price

    def remove_videogame(self, game: Videogame):
        """Remove a videogame from the machine.

        Args:
            game: The Videogame object to remove.
        """
        if game in self.videogames:
            self.videogames.remove(game)
            self.base_price -= game.price

    def calculate_total_price(self) -> float:
        """Calculate the total price of the machine including all videogames.

        Returns:
            The total price of the machine.
        """
        return self.base_price

class PredefinedMachine(abc.ABC):
    """Abstract base class for predefined machine types."""

    @abc.abstractmethod
    def create_machine(self, material: str, color: str) -> Machine:
        """Create a machine of the predefined type.

        Args:
            material: The material to use for the machine.
            color: The color of the machine.

        Returns:
            A Machine object of the predefined type.
        """
        pass

class DanceRevolutionMachine(PredefinedMachine):
    """Represents a Dance Revolution arcade machine."""

    def create_machine(self, material: str, color: str) -> Machine:
        """Create a Dance Revolution machine.

        Args:
            material: The material to use for the machine.
            color: The color of the machine.

        Returns:
            A Machine object configured as a Dance Revolution machine.
        """
        machine = Machine(material, Dimensions(2.0, 1.5, 2.2), 200, 1000, 8, 2, 5000, color)
        machine.difficulties = ["Easy", "Medium", "Hard"]
        machine.arrow_cardinalities = 4
        machine.controls_price = 500
        return machine

class ClassicalArcadeMachine(PredefinedMachine):
    """Represents a Classical Arcade machine."""

    def create_machine(self, material: str, color: str) -> Machine:
        """Create a Classical Arcade machine.

        Args:
            material: The material to use for the machine.
            color: The color of the machine.

        Returns:
            A Machine object configured as a Classical Arcade machine.
        """
        machine = Machine(material, Dimensions(0.8, 0.6, 1.8), 100, 500, 4, 1, 3000, color)
        return machine

    @staticmethod
    def make_vibration():
        """Simulate the machine's vibration feature."""
        print("Classical Arcade is vibrating!")

    @staticmethod
    def sound_record_alert():
        """Simulate the machine's sound record alert."""
        print("Classical Arcade sound record alert!")

class ShootingMachine(PredefinedMachine):
    """Represents a Shooting arcade machine."""

    def create_machine(self, material: str, color: str) -> Machine:
        """Create a Shooting machine.

        Args:
            material: The material to use for the machine.
            color: The color of the machine.

        Returns:
            A Machine object configured as a Shooting machine.
        """
        machine = Machine(material, Dimensions(1.5, 1.2, 2.0), 150, 800, 8, 2, 4000, color)
        machine.number_of_guns = 2
        machine.target_type = "Moving"
        return machine

class RacingMachine(PredefinedMachine):
    """Represents a Racing arcade machine."""

    def create_machine(self, material: str, color: str) -> Machine:
        """Create a Racing machine.

        Args:
            material: The material to use for the machine.
            color: The color of the machine.

        Returns:
            A Machine object configured as a Racing machine.
        """
        machine = Machine(material, Dimensions(2.0, 1.8, 1.5), 180, 1200, 16, 4, 6000, color)
        machine.steering_type = "Force Feedback"
        machine.number_of_seats = 1
        return machine

class VirtualRealityMachine(PredefinedMachine):
    """Represents a Virtual Reality arcade machine."""

    def create_machine(self, material: str, color: str) -> Machine:
        """Create a Virtual Reality machine.

        Args:
            material: The material to use for the machine.
            color: The color of the machine.

        Returns:
            A Machine object configured as a Virtual Reality machine.
        """
        machine = Machine(material, Dimensions(2.5, 2.5, 2.2), 220, 1500, 32, 8, 8000, color)
        machine.glasses_type = "OLED"
        machine.glasses_resolution = "4K"
        machine.glasses_price = 1000
        return machine

class MaterialDecorator(abc.ABC):
    """Abstract base class for material decorators."""

    def __init__(self, machine: Machine):
        """Initialize the MaterialDecorator.

        Args:
            machine: The Machine object to decorate.
        """
        self.machine = machine

    @abc.abstractmethod
    def adjust_weight(self):
        """Adjust the weight of the machine based on the material."""
        pass

    @abc.abstractmethod
    def adjust_price(self):
        """Adjust the price of the machine based on the material."""
        pass

    @abc.abstractmethod
    def adjust_power_consumption(self):
        """Adjust the power consumption of the machine based on the material."""
        pass

class WoodMaterialDecorator(MaterialDecorator):
    """Material decorator for wooden machines."""

    def adjust_weight(self):
        """Increase the weight by 10%."""
        self.machine.weight *= 1.1

    def adjust_price(self):
        """Decrease the price by 5%."""
        self.machine.base_price *= 0.95

    def adjust_power_consumption(self):
        """Increase the power consumption by 15%."""
        self.machine.power_consumption *= 1.15

class AluminiumMaterialDecorator(MaterialDecorator):
    """Material decorator for aluminium machines."""

    def adjust_weight(self):
        """Decrease the weight by 5%."""
        self.machine.weight *= 0.95

    def adjust_price(self):
        """Increase the price by 10%."""
        self.machine.base_price *= 1.1

    def adjust_power_consumption(self):
        """No change in power consumption."""
        pass

class CarbonFiberMaterialDecorator(MaterialDecorator):
    """Material decorator for carbon fiber machines."""

    def adjust_weight(self):
        """Decrease the weight by 15%."""
        self.machine.weight *= 0.85

    def adjust_price(self):
        """Increase the price by 20%."""
        self.machine.base_price *= 1.2

    def adjust_power_consumption(self):
        """Decrease the power consumption by 10%."""
        self.machine.power_consumption *= 0.9

class MachineFactory:
    """Factory class for creating arcade machines."""

    @staticmethod
    def create_machine(machine_type: str, material: str, color: str) -> Optional[Machine]:
        """Create a machine of the specified type with the given material and color.

        Args:
            machine_type: The type of machine to create.
            material: The material to use for the machine.
            color: The color of the machine.

        Returns:
            A Machine object of the specified type, or None if the type is invalid.
        """
        predefined_machines = {
            "DanceRevolution": DanceRevolutionMachine(),
            "ClassicalArcade": ClassicalArcadeMachine(),
            "Shooting": ShootingMachine(),
            "Racing": RacingMachine(),
            "VirtualReality": VirtualRealityMachine()
        }

        machine_creator = predefined_machines.get(machine_type)
        if not machine_creator:
            return None

        machine = machine_creator.create_machine(material, color)

        material_decorators = {
            "wood": WoodMaterialDecorator,
            "aluminium": AluminiumMaterialDecorator,
            "carbon fiber": CarbonFiberMaterialDecorator
        }

        decorator = material_decorators.get(material.lower())
        if decorator:
            decorated_machine = decorator(machine)
            decorated_machine.adjust_weight()
            decorated_machine.adjust_price()
            decorated_machine.adjust_power_consumption()

        return machine

class CatalogManager:
    """Manages the catalog of arcade machines."""

    def __init__(self):
        """Initialize the CatalogManager."""
        self.machines: List[Machine] = []

    def register_machine(self, machine: Machine):
        """Register a new machine in the catalog.

        Args:
            machine: The Machine object to register.
        """
        self.machines.append(machine)

    def search_by_videogame_count(self, count: int) -> List[Machine]:
        """Search for machines with a specific number of videogames.

        Args:
            count: The number of videogames to search for.

        Returns:
            A list of Machine objects with the specified number of videogames.
        """
        return [m for m in self.machines if len(m.videogames) == count]

    def search_by_material(self, material: str) -> List[Machine]:
        """Search for machines made of a specific material.

        Args:
            material: The material to search for.

        Returns:
            A list of Machine objects made of the specified material.
        """
        return [m for m in self.machines if m.material.lower() == material.lower()]

    def search_by_videogame_name(self, name: str) -> List[Machine]:
        """Search for machines containing a specific videogame.

        Args:
            name: The name of the videogame to search for.

        Returns:
            A list of Machine objects containing the specified videogame.
        """
        return [m for m in self.machines if any(v.name.lower() == name.lower() for v in m.videogames)]

    def search_by_price_range(self, min_price: float, max_price: float) -> List[Machine]:
        """Search for machines within a specific price range.

        Args:
            min_price: The minimum price.
            max_price: The maximum price.

        Returns:
            A list of Machine objects within the specified price range.
        """
        return [m for m in self.machines if min_price <= m.calculate_total_price() <= max_price]

    def search_by_weight_range(self, min_weight: float, max_weight: float) -> List[Machine]:
        """Search for machines within a specific weight range.

        Args:
            min_weight: The minimum weight in kg.
            max_weight: The maximum weight in kg.

        Returns:
            A list of Machine objects within the specified weight range.
        """
        return [m for m in self.machines if min_weight <= m.weight <= max_weight]

    def search_by_power_consumption_range(self, min_power: float, max_power: float) -> List[Machine]:
        """Search for machines within a specific power consumption range.

        Args:
            min_power: The minimum power consumption in watts.
            max_power: The maximum power consumption in watts.

        Returns:
            A list of Machine objects within the specified power consumption range.
        """
        return [m for m in self.machines if min_power <= m.power_consumption <= max_power]