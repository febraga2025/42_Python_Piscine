#!/usr/bin/env python3
"""A simple script to introduce garden plant data."""


def main() -> None:
    """Entry point of the garden intro program."""
    p_name = 'Rose'
    p_height = 25
    p_age = 30

    print('=== Welcome to My Garden ===')
    print(f'Plant: {p_name}')
    print(f'Height: {p_height}cm')
    print(f'Age: {p_age} days')
    print('=== End of Program ===')


if __name__ == "__main__":
    main()
