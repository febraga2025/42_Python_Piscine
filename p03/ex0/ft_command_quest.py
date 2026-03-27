#!/usr/bin/env python3
"""Module to demonstrate command-line argument processing using sys.argv."""
import sys


def main() -> None:
    """Processes and displays arguments received from the command line."""
    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
        return

    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")

    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
