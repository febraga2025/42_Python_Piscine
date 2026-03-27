#!/usr/bin/env python3
"""Module to track and analyze unique player achievements using sets."""


def main() -> None:
    """Demonstrates set operations: union, intersection, and difference."""
    alice: set[str] = {"first_kill", "level_10", "treasure_hunter",
                       "speed_demon"}
    bob: set[str] = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie: set[str] = {
        "level_10", "treasure_hunter", "boss_slayer",
        "speed_demon", "perfectionist"
    }

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_unique = alice.union(bob, charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    common_all = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common_all}")

    rare = ((alice - bob - charlie) | (bob - alice - charlie) |
            (charlie - alice - bob))
    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
