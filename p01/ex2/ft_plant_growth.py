#!/usr/bin/env python3
"""Module to simulate plant growth and aging over time."""


class Plant:
    """Blueprint for a plant that can grow and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with name, height (cm), and age (days)."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, cm: int = 1) -> None:
        """Increase the plant's height."""
        self.height += cm

    def age_up(self, days: int = 1) -> None:
        """Increase the plant's age."""
        self.age += days

    def get_info(self) -> str:
        """Return formatted status of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    """Simulates a week in the life of the garden."""
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(rose.get_info())

    days_to_simulate: int = 6
    growth_per_day: int = 1

    for _ in range(days_to_simulate):
        rose.age_up(1)
        rose.grow(growth_per_day)

    print(f"=== Day {1 + days_to_simulate} ===")
    print(rose.get_info())
    print(f"Growth this week: +{days_to_simulate * growth_per_day}cm")


if __name__ == "__main__":
    main()
