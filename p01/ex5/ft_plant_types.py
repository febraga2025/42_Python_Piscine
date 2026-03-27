#!/usr/bin/env python3
"""Module demonstrating Inheritance with specialized Plant types."""


class Plant:
    """Base class for all plants in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize common plant attributes."""
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """A specialized plant that can bloom."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize flower with parent traits plus color."""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Display blooming information."""
        print(f'{self.name} (Flower): {self.height}cm, {self.age} days, '
              f'{self.color} color')
        print(f'{self.name} is blooming beautifully!')


class Tree(Plant):
    """A specialized plant that provides shade."""

    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> None:
        """Initialize tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter: int = diameter

    def produce_shade(self) -> None:
        """Calculate and display shade area."""
        shade_area = int(self.trunk_diameter * 1.56)
        print(f'{self.name} (Tree): {self.height}cm, '
              f'{self.age} days, {self.trunk_diameter}cm diameter')
        print(f'{self.name} provides {shade_area} square meters of shade')


class Vegetable(Plant):
    """A specialized plant that is edible."""

    def __init__(self, name: str, h: int, a: int,
                 season: str, nut: str) -> None:
        """Initialize vegetable with harvest and nutritional data."""
        super().__init__(name, h, a)
        self.harvest_season: str = season
        self.nutritional_value: str = nut

    def show_info(self) -> None:
        """Display vegetable details."""
        print(f'{self.name} (Vegetable): {self.height}cm, {self.age} days, '
              f'{self.harvest_season} harvest')
        print(f'{self.name} is rich in {self.nutritional_value}')


def main() -> None:
    """Entry point for testing specialized plants."""
    print('=== Garden Plant Types ===')
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 30, 15, "white")

    oak = Tree("Oak", 500, 1825, 50)
    pinus = Tree("Pinus", 800, 3650, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 70, "winter", "vitamin A")

    rose.bloom()
    tulip.bloom()
    print()
    oak.produce_shade()
    pinus.produce_shade()
    print()
    tomato.show_info()
    carrot.show_info()


if __name__ == "__main__":
    main()
