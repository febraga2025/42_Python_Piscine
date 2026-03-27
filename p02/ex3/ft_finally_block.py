#!/usr/bin/env python3
"""Module to demonstrate the use of finally blocks for resource cleanup."""


def water_plants(plant_list: list[str | None]) -> None:
    """
    Simulates watering a list of plants.
    Uses a finally block to ensure the system is closed regardless of errors.
    """
    try:
        print('Opening watering system')
        for plant in plant_list:
            if plant is None:
                raise ValueError('Cannot water None - invalid plant!')
            print(f'Watering {plant}')
    except ValueError as error:
        print(f'Error: {error}')
    finally:
        print('Closing watering system (cleanup)')


def test_watering_system() -> None:
    """Tests the watering system with both valid and invalid inputs."""
    print('=== Garden Watering System ===')

    print('Testing normal watering...')
    water_plants(['tomato', 'lettuce', 'carrots'])
    print('Watering completed successfully!')

    print('\nTesting with error...')
    water_plants(['tomato', None, 'carrots'])
    print('Cleanup always happens, even with errors!')


if __name__ == '__main__':
    test_watering_system()
