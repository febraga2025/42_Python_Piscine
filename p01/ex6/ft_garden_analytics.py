#!/usr/bin/env python3
"""Comprehensive Garden Analytics Platform."""


class Plant:
    """Base plant class with common attributes."""
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.plant_type: str = "regular"

    def grow(self, amount: int = 1) -> None:
        """Increase height of the plant."""
        self.height += amount

    def score(self) -> int:
        """Return basic score based on height."""
        return self.height

    def __str__(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Plant that has flowers and a specific color."""
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.plant_type: str = "flowering"

    def __str__(self) -> str:
        return (f"- {self.name}: {self.height}cm,"
                f" {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """High-value flower with extra points."""
    def __init__(self, name: str, height: int, color: str, pts: int) -> None:
        super().__init__(name, height, color)
        self.points: int = pts
        self.plant_type: str = "prize"

    def score(self) -> int:
        """Calculates score including bonus prize points."""
        return self.height + self.points

    def __str__(self) -> str:
        return (
            f"- {self.name}: {self.height}cm, {self.color} flowers "
            f"(blooming), Prize points: {self.points}"
        )


class GardenManager:
    """Manages multiple gardens and their analytics."""
    total_gardens: int = 0

    class GardenStats:
        """Helper class for garden statistics."""
        @staticmethod
        def validate_height(height: int) -> bool:
            """Check if a height value is valid."""
            return height > 0

        @staticmethod
        def garden_score(plants: list[Plant]) -> int:
            """Sum the scores of all plants in a collection."""
            return sum(plant.score() for plant in plants)

    def __init__(self, owner_name: str) -> None:
        self.owner_name: str = owner_name
        self.plants: list[Plant] = []
        self.total_growth: int = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant instance to the garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_plants(self, amount: int) -> None:
        """Apply growth to all plants in the garden."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            print(f"{plant.name} grew {amount}cm")
        self.total_growth += amount * len(self.plants)

    def check_all_height(self) -> bool:
        """Validate the height of every plant using the nested helper."""
        return all(
            GardenManager.GardenStats.validate_height(p.height)
            for p in self.plants
        )

    def plant_type_counts(self) -> tuple[int, int, int]:
        """Count occurrences of each plant type."""
        reg, flow, prz = 0, 0, 0
        for p in self.plants:
            if p.plant_type == "prize":
                prz += 1
            elif p.plant_type == "flowering":
                flow += 1
            else:
                reg += 1
        return reg, flow, prz

    def generate_report(self) -> None:
        """Display a full analytical report of the garden."""
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(p)
        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        r, f, p_count = self.plant_type_counts()
        print(f"Plant types: {r} regular, {f} flowering,"
              f" {p_count} prize flowers")
        print(f"Height validation test: {self.check_all_height()}")

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list['GardenManager']:
        """Factory method to create multiple managers at once."""
        return [cls(owner) for owner in owners]


def main() -> None:
    """Execution demo for the analytics platform."""
    alice, bob = GardenManager.create_garden_network(["Alice", "Bob"])

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    bob.add_plant(Plant("Mint", 32))
    bob.add_plant(FloweringPlant("Lavender", 60, "purple"))

    print("=== Garden Management System Demo ===")
    alice.grow_plants(1)
    alice.generate_report()

    a_score = GardenManager.GardenStats.garden_score(alice.plants)
    b_score = GardenManager.GardenStats.garden_score(bob.plants)
    print(f"Garden scores - Alice: {a_score}, Bob: {b_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
