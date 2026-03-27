#!/usr/bin/env python3
"""Module to validate agricultural temperature readings."""


def check_temperature(temp_str: str) -> int:
    """
    Validates if a string is a valid temperature within 0-40 degrees.
    Raises ValueError for invalid inputs or out-of-range values.
    """
    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")

    return temperature


def test_temperature_input() -> None:
    """Tests the temperature checker with various inputs."""
    print('=== Garden Temperature Checker ===')
    tests = ['25', 'abc', '100', '-50']

    for value in tests:
        print(f'Testing temperature: {value}')
        try:
            temp = check_temperature(value)
            print(f'Temperature {temp}°C is perfect for plants!')
        except ValueError as e:
            print(f'Error: {e}')

    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature_input()
