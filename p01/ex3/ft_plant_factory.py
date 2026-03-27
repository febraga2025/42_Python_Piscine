#!/usr/bin/env python3
"""Module for the Plant Factory exercise: bulk instantiation of plants."""


class Plant:
    """Represents a plant, ready to be created with initial values."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize the plant instance.
        This makes the plant 'ready to use' immediately.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return a string formatted for the factory output."""
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def main() -> None:
    """Main function to simulate a plant factory production."""
    plant_factory: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")

    for index in range(len(plant_factory)):
        print(plant_factory[index].get_info())

    print(f"Total plants created: {len(plant_factory)}")


if __name__ == "__main__":
    main()
