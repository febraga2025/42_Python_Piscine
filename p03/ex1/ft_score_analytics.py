#!/usr/bin/env python3
"""Module for analyzing player scores using lists and basic statistics."""
import sys


def process_scores(args: list[str]) -> list[int]:
    """Converts a list of strings to a list of integers,
    skipping invalid values."""
    scores = []
    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            continue
    return scores


def main() -> None:
    """Main function to calculate and display player score analytics."""
    print("=== Player Score Analytics ===")

    args = sys.argv[1:]

    if not args:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    scores = process_scores(args)
    if not scores:
        return

    count = len(scores)
    total = sum(scores)
    average = total / count
    high = max(scores)
    low = min(scores)
    score_range = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
