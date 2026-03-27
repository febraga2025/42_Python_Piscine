#!/usr/bin/env python3
"""Module to demonstrate custom exception hierarchies in a garden system."""


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


def trigger_plant_error() -> None:
    """Raises a PlantError with a specific message."""
    raise PlantError('The tomato plant is wilting!')


def trigger_water_error() -> None:
    """Raises a WaterError with a specific message."""
    raise WaterError('Not enough water in the tank!')


def test_custom_errors() -> None:
    """Demonstrates how to catch specific and inherited custom errors."""
    print('=== Custom Garden Errors Demo ===')

    print('Testing PlantError...')
    try:
        trigger_plant_error()
    except PlantError as error:
        print(f'Caught PlantError: {error}')

    print('Testing WaterError...')
    try:
        trigger_water_error()
    except WaterError as error:
        print(f'Caught WaterError: {error}')

    print('Testing catching all garden errors...')
    try:
        trigger_plant_error()
    except GardenError as error:
        print(f'Caught a garden error: {error}')

    try:
        trigger_water_error()
    except GardenError as error:
        print(f'Caught a garden error: {error}')

    print('All custom error types work correctly!')


if __name__ == '__main__':
    test_custom_errors()
