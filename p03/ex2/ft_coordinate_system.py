#!/usr/bin/env python3
"""Module to manage 3D coordinates using
immutable tuples and math operations."""
import math


def coordinates(coord_str: str) -> tuple[int, int, int]:
    """Parses a comma-separated string into a 3D coordinate tuple."""
    parts = coord_str.split(',')
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def calc_distance(coord: tuple[int, int, int]) -> float:
    """Calculates the Euclidean distance from the origin (0, 0, 0)."""
    x, y, z = coord
    return math.sqrt(x**2 + y**2 + z**2)


def main() -> None:
    """Demonstrates tuple creation, unpacking, and distance calculation."""
    print("=== Game Coordinate System ===\n")

    initial_pos = (10, 20, 5)
    print(f"Position created: {initial_pos}")

    dist_initial = calc_distance(initial_pos)
    print(f"Distance between (0, 0, 0) and {initial_pos}: {dist_initial:.2f}")

    coord_str = "3,4,0"
    print(f'\nParsing coordinates: "{coord_str}"')

    parsed_pos = coordinates(coord_str)
    print(f"Parsed position: {parsed_pos}")

    dist_parsed = calc_distance(parsed_pos)
    print(f"Distance between (0, 0, 0) and {parsed_pos}: {dist_parsed:.1f}")

    print('\nParsing invalid coordinates: "abc,def,ghi"')
    try:
        coordinates("abc,def,ghi")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = parsed_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
