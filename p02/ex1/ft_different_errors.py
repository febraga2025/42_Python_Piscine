#!/usr/bin/env python3
"""
Module to demonstrate different types of built-in Python exceptions
and how to handle them individually or in groups.
"""


def garden_operations() -> None:
    """
    Triggers and catches four common types of Python errors to demonstrate
    how the exception handling system works.
    """
    print('Testing ValueError...')
    try:
        int('abc')
    except ValueError as error:
        print(f'Caught ValueError: {error}')

    print('\nTesting ZeroDivisionError...')
    try:
        _ = 1 / 0
    except ZeroDivisionError as error:
        print(f'Caught ZeroDivisionError: {error}')

    print('\nTesting FileNotFoundError...')
    try:
        file_handle = open('missing.txt')
        file_handle.close()
    except FileNotFoundError as error:
        print(f'Caught FileNotFoundError: {error}')

    print('\nTesting KeyError...')
    try:
        plants = {'sunflower': 'yellow'}
        _ = plants['missing_plant']
    except KeyError as error:
        print(f'Caught KeyError: {error}')

    print('\nTesting multiple errors together...')
    try:
        int('abc')
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print('Caught an error, but program continues!')


def test_error_types() -> None:
    """
    Runner function to display the garden error types demo.
    """
    print('=== Garden Error Types Demo ===')
    garden_operations()
    print('All error types tested successfully!')


if __name__ == '__main__':
    test_error_types()
