#!/usr/bin/env python3
"""Module for a Garden Management System exactly matching PDF requirements."""


class GardenError(Exception):
    """Base exception for all garden-related issues."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception raised for specific plant problems."""
    pass


class WaterError(GardenError):
    """Exception raised for irrigation or water tank issues."""
    pass


class GardenManager:
    """Manages garden operations including adding,
    watering and checking plants."""

    def __init__(self) -> None:
        """Initializes the manager with an empty list of plants."""
        self.plants: list[str] = []

    def add_plant(self, name: str) -> None:
        """Adds a plant to the garden if the name is valid."""
        if not name:
            raise PlantError('Plant name cannot be empty!')
        self.plants.append(name)
        print(f'Added {name} successfully')

    def water_plants(self) -> None:
        """Simulates watering all plants with mandatory cleanup."""
        print('Opening watering system')
        try:
            for plant in self.plants:
                print(f'Watering {plant} - success')
        finally:
            print('Closing watering system (cleanup)\n')

    def check_plant_health(
        self,
        plant_name: str,
        water_level: int,
        sunlight_hours: int
    ) -> str:
        """Validates plant health parameters and returns a status string."""
        if not plant_name:
            raise PlantError('Plant name cannot be empty!')
        if water_level < 1:
            raise ValueError(f'Water level {water_level} is too low (min 1)')
        if water_level > 10:
            raise ValueError(f'Water level {water_level} is too high (max 10)')
        if sunlight_hours < 2:
            raise ValueError(f'Sunlight hours {sunlight_hours}'
                             ' is too low (min 2)')
        if sunlight_hours > 12:
            raise ValueError(
                f'Sunlight hours {sunlight_hours} is too high (max 12)'
            )
        return (f'{plant_name}: healthy '
                f'(water: {water_level}, sun: {sunlight_hours})')


def test_garden_management() -> None:
    """Runs a complete simulation matching the PDF example output."""
    gm = GardenManager()
    print('=== Garden Management System ===\n')

    print('Adding plants to garden...')
    for name in ['tomato', 'lettuce', '']:
        try:
            gm.add_plant(name)
        except PlantError as error:
            print(f'Error adding plant: {error}')

    print('\nWatering plants...')
    try:
        gm.water_plants()
    except WaterError as error:
        print(f'Error watering: {error}')

    print('Checking plant health...')
    try:
        print(gm.check_plant_health('tomato', 5, 8))
    except (GardenError, ValueError) as error:
        print(f'Error checking tomato: {error}')

    try:
        print(gm.check_plant_health('lettuce', 15, 8))
    except (GardenError, ValueError) as error:
        print(f'Error checking lettuce: {error}')

    print('\nTesting error recovery...')
    try:
        raise WaterError('Not enough water in tank')
    except GardenError as error:
        print(f'Caught GardenError: {error}')
        print('System recovered and continuing...')

    print('\nGarden management system test complete!')


if __name__ == '__main__':
    test_garden_management()
