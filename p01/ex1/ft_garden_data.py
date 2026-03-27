#!/usr/bin/env python3
"""Module for managing garden plant data using a Class blueprint."""


class Plant:
    """Represents a plant with a name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant instance."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return a formatted string with plant information."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    """Main function to register and display plants."""
    my_plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for index in range(len(my_plants)):
        print(my_plants[index].get_info())


if __name__ == "__main__":
    main()
