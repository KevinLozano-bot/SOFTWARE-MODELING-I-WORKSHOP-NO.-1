"""

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
from abc import ABC, abstractmethod

class GamingConsole(ABC):
    """
    Abstract base class for a gaming console.

    Defines the structure and methods that all gaming consoles must implement.
    """

    @abstractmethod
    def display_specs(self):
        """
        Display the specifications of the gaming console.

        This method should be implemented to provide detailed specifications of the console.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def storage_options(self):
        """
        Display available storage options for the console.

        This method should be implemented to list all the storage options available for the console.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def show_compatibility(self):
        """
        Display backward and forward compatibility of the console.

        This method should be implemented to show how the console is compatible with previous and future generations of games.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def demo_info(self):
        """
        Provide information on how to access console demos.

        This method should be implemented to provide details on demo availability and testing opportunities for the console.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def network_config(self):
        """
        Display network configuration options for the console.

        This method should be implemented to show network configuration options and features of the console.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def compare(self):
        """
        Compare the console with other consoles.

        This method should be implemented to compare the console's features and performance with other consoles.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def customization(self):
        """
        Display customization options for the gaming console.

        This method should be implemented to show available customization options and accessories for the console.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def durability(self):
        """
        Display durability information for the gaming console.

        This method should be implemented to provide details on the console's durability and build quality.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def accessibility(self):
        """
        Display accessibility features of the gaming console.

        This method should be implemented to show the accessibility features and options available for users with disabilities.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def ai_technologies(self):
        """
        Display AI technologies used in the gaming console.

        This method should be implemented to provide information on AI technologies integrated into the console.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def audio_options(self):
        """
        Display audio options for the gaming console.

        This method should be implemented to show audio features and customization options available with the console.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def power_consumption(self):
        """
        Display power consumption and efficiency of the gaming console.

        This method should be implemented to provide information on the console's power consumption and energy efficiency.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def security(self):
        """
        Display security options for the gaming console.

        This method should be implemented to show the console's security features and options.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def ray_tracing_performance(self):
        """
        Display ray-tracing performance details of the gaming console.

        This method should be implemented to provide information on the console's ray-tracing capabilities and performance metrics.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

    @abstractmethod
    def sales_guidance(self):
        """
        Provide sales guidance for the gaming console.

        This method should be implemented to offer guidance and support for sales staff and customers.

        Raises:
            NotImplementedError: This method should be overridden in a concrete subclass.
        """
        pass

class AdvancedGamingConsole(GamingConsole):
    """
    Concrete class that implements the abstract methods of the GamingConsole class.

    Represents an advanced gaming console with specific attributes and methods.
    """

    def display_specs(self):
        """
        Displays the main specifications of the gaming console.

        This method provides details on the console's processor, RAM, graphics, and storage.

        Returns:
            None

        Raises:
            None
        """
        print("\nConsole: NextGen Gaming Console")
        print("Processor: Octa-core 3.5GHz")
        print("RAM: 16GB GDDR6")
        print("Graphics: Custom RDNA 2 GPU")
        print("Storage: 1TB NVMe SSD")

    def storage_options(self):
        """
        Displays the available storage options for the gaming console.

        This method lists all the storage options available for the console, including default and upgradeable options.

        Returns:
            None

        Raises:
            None
        """
        print("\nStorage Options:")
        print("1. 1TB NVMe SSD (Default)")
        print("2. 2TB NVMe SSD")
        print("3. 4TB NVMe SSD")
        print("4. 1TB NVMe SSD + 2TB HDD")
        print("Upgradeable with additional M.2 SSD slot")

    def show_compatibility(self):
        """
        Displays backward and forward compatibility of the gaming console.

        This method provides information on how the console supports games from previous generations and future releases.

        Returns:
            None

        Raises:
            None
        """
        print("\nBackward Compatible: True")
        print("Forward Compatible: True")
        print("Supports games from previous generation and optimized for future releases")

    def demo_info(self):
        """
        Provides information on how to access console demos.

        This method offers details on demo availability and testing opportunities for the console.

        Returns:
            None

        Raises:
            None
        """
        print("\nDemo videos and game testing:")
        print("1. Visit our YouTube channel for gameplay demos")
        print("2. Schedule an in-store demo for hands-on experience")
        print("3. 7-day trial period available with purchase")

    def network_config(self):
        """
        Displays the network features and configuration options.

        This method provides details on network options including Wi-Fi, Ethernet, IPv6 support, and built-in VPN.

        Returns:
            None

        Raises:
            None
        """
        print("\nNetwork Configuration Options:")
        print("1. Wi-Fi 6 (802.11ax) support")
        print("2. 2.5Gbps Ethernet port")
        print("3. IPv6 Support: True")
        print("4. Built-in VPN for secure gaming")

    def compare(self):
        """
        Compares the console with other consoles.

        This method provides a comparison of the console's performance, graphics, and load times with those of other consoles.

        Returns:
            None

        Raises:
            None
        """
        print("\nComparison with other consoles:")
        print("1. Performance: 20% faster than Competitor X")
        print("2. Graphics: 15% better visual quality than Competitor Y")
        print("3. Load Times: 30% faster than previous generation")
        print("For detailed comparisons, visit our website")

    def customization(self):
        """
        Displays customization options for the gaming console.

        This method lists all available customization options, including faceplates, RGB lighting, and controller skins.

        Returns:
            None

        Raises:
            None
        """
        print("\nCustomization Options:")
        print("1. Custom faceplates")
        print("2. RGB lighting")
        print("3. Controller skins")
        print("\nAvailable Accessories:")
        print("1. Pro Controller")
        print("2. VR Headset")
        print("3. Racing Wheel")

    def durability(self):
        """
        Displays durability information for the gaming console.

        This method provides details on the console's build quality, including drop test certification and resistance to dust and water.

        Returns:
            None

        Raises:
            None
        """
        print("\nDurability Information:")
        print("1. Military-grade drop test certified")
        print("2. Dust and water-resistant (IP54)")
        print("3. 5-year warranty included")

    def accessibility(self):
        """
        Displays accessibility features of the gaming console.

        This method shows the accessibility features available for users with disabilities, such as screen readers and customizable button mapping.

        Returns:
            None

        Raises:
            None
        """
        print("\nAccessibility Features:")
        print("1. Compatible with screen readers")
        print("2. Supports closed captioning")
        print("3. Customizable button mapping")
        print("4. Voice control support")

    def ai_technologies(self):
        """
        Displays AI technologies used in the gaming console.

        This method provides information on the AI technologies integrated into the console, including NPC behavior and procedural content generation.

        Returns:
            None

        Raises:
            None
        """
        print("\nAI Technologies in Games:")
        print("1. Advanced NPC behavior")
        print("2. Dynamic difficulty adjustment")
        print("3. Procedural content generation")
        print("4. Real-time language translation")

    def audio_options(self):
        """
        Displays audio options for the gaming console.

        This method provides details on audio features such as 3D spatial audio and customizable EQ settings.

        Returns:
            None

        Raises:
            None
        """
        print("\n3D Sound and Audio Customization:")
        print("1. 3D Spatial Audio support")
        print("2. Custom EQ settings")
        print("3. Multi-output audio (headphones, speakers, HDMI)")
        print("4. Voice chat noise cancellation")

    def power_consumption(self):
        """
        Displays power consumption and energy efficiency of the gaming console.

        This method provides information on the console's power consumption in various modes and its overall energy efficiency rating.

        Returns:
            None

        Raises:
            None
        """
        print(f"\nEnergy Efficiency: 80 PLUS Platinum")
        print("Power Consumption:")
        print("1. Standby: 0.5W")
        print("2. Idle: 30W")
        print("3. Gaming: 100-180W depending on the game")
        print("4. Energy-saving mode available")

    def security(self):
        """
        Displays security options for the gaming console.

        This method provides details on the console's security features, including two-factor authentication and biometric login.

        Returns:
            None

        Raises:
            None
        """
        print("\nAdvanced Security Options:")
        print("1. Two-factor authentication")
        print("2. Biometric login (fingerprint)")
        print("3. Parental controls")
        print("4. Encrypted storage")

    def ray_tracing_performance(self):
        """
        Displays ray-tracing performance details of the gaming console.

        This method provides information on the console's ray-tracing capabilities, including support for 4K resolution and performance improvements.

        Returns:
            None

        Raises:
            None
        """
        print("\nRay-Tracing Performance:")
        print("1. Supports real-time ray tracing up to 4K/60fps")
        print("2. 50% faster ray tracing performance than previous gen")
        print("3. Compatible with all major ray tracing APIs")

    def sales_guidance(self):
        """
        Provides sales guidance for the gaming console.

        This method offers guidance and support for sales staff, including in-store demonstrations and online chat support.

        Returns:
            None

        Raises:
            None
        """
        print("\nSales Staff Guidance:")
        print("1. In-store demonstrations available")
        print("2. Online chat support 24/7")
        print("3. Detailed user manual and quick start guide included")
        print("4. Video tutorials available on our website")
