#!/usr/bin/env python3
"""Module for SecurePlant: implementing data encapsulation and validation."""


class SecurePlant:
    """A plant class that protects its data from invalid values."""

    def __init__(self, name: str) -> None:
        """Initialize the plant with a name and protected attributes."""
        self.name: str = name
        self._height: int = 0
        self._age: int = 0
        print(f'Plant created: {self.name}')

    def set_height(self, height: int) -> None:
        """Validate and set the plant height."""
        if height < 0:
            print(f'Invalid operation attempted: height {height}cm [REJECTED]')
            print('Security: Negative height rejected')
        else:
            self._height = height
            print(f'Height updated: {height}cm [OK]')

    def set_age(self, age: int) -> None:
        """Validate and set the plant age."""
        if age < 0:
            print(f'Invalid operation attempted: age {age} days [REJECTED]')
            print('Security: Negative age rejected')
        else:
            self._age = age
            print(f'Age updated: {age} days [OK]')

    def get_height(self) -> int:
        """Safe access to the protected height attribute."""
        return self._height

    def get_age(self) -> int:
        """Safe access to the protected age attribute."""
        return self._age


def main() -> None:
    """Demonstrates the security system in action."""
    print("=== Garden Security System ===")
    my_plant = SecurePlant("Rose")

    my_plant.set_height(25)
    my_plant.set_age(30)

    my_plant.set_height(-5)

    print(f'Current plant: {my_plant.name} '
          f'({my_plant.get_height()}cm, '
          f'{my_plant.get_age()} days)')


if __name__ == "__main__":
    main()
