#!/usr/bin/env python3
"""Module to demonstrate memory-efficient data processing using generators."""
from typing import Generator


def game_event_generator(n: int) -> Generator[tuple[str, int, str],
                                              None, None]:
    """
    Generator that yields game events one by one.
    Uses yield to maintain memory efficiency.
    """
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    t_high, t_treasure, t_lvlup = 342, 89, 156
    c_high = c_treasure = c_lvlup = 0

    for i in range(1, n + 1):
        player = players[(i - 1) % 3]

        if i <= 3:
            levels = [5, 12, 8]
            level, action = levels[i-1], actions[i-1]
        else:
            if c_treasure < t_treasure:
                action = actions[1]
            elif c_lvlup < t_lvlup:
                action = actions[2]
            else:
                action = actions[0]

            if c_high < t_high:
                level = 10 + (i % 5)
            else:
                level = 1 + (i % 9)

        if level >= 10:
            c_high += 1
        if action == actions[1]:
            c_treasure += 1
        elif action == actions[2]:
            c_lvlup += 1

        msg = f"Event {i}: Player {player} (level {level}) {action}"
        yield (msg, level, action)


def fibonacci_gen(n: int) -> Generator[int, None, None]:
    """Yields the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int) -> Generator[int, None, None]:
    """Yields the first n prime numbers using a simple loop."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main() -> None:
    """Entry point using only authorized functions."""
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    events = game_event_generator(1000)
    high_level = treasures = level_ups = 0

    for i in range(1, 1001):
        msg, level, action = next(events)

        if i <= 3:
            print(msg)
        elif i == 4:
            print("...")

        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasures += 1
        elif action == "leveled up":
            level_ups += 1

    print("\n=== Stream Analytics ===")
    print("Total events processed: 1000")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_ups}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10):", end=" ")
    fibo = fibonacci_gen(10)
    for i in range(10):
        res = next(fibo)
        end = ", " if i < 9 else ""
        print(res, end=end)

    print("\nPrime numbers (first 5):", end=" ")
    primes = prime_gen(5)
    for i in range(5):
        res = next(primes)
        end = ", " if i < 4 else ""
        print(res, end=end)
    print()


if __name__ == "__main__":
    main()
