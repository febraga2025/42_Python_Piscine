#!/usr/bin/env python3
"""
Module to demonstrate data transformation using comprehensions.
Calibrated to match the visual and logical output of the PDF.
"""


def run_analytics() -> None:
    """
    Main analytics engine demonstrating list, dict, and set comprehensions.
    """
    players_data = [
        ("alice", 2300, "north", 5),
        ("bob", 1800, "central", 3),
        ("charlie", 2150, "north", 7),
        ("diana", 2050, "east", 4),
        ("eve", 1900, "east", 2),
        ("frank", 900, "central", 1)
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p[0] for p in players_data[:4] if p[1] >= 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p[1] * 2 for p in players_data[:4]]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p[0] for p in players_data[:3]]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p[0]: p[1] for p in players_data[:3]}
    print(f"Player scores: {player_scores}")

    cats = ["high" if p[1] >= 2000 else "medium" if p[1] >= 1000 else "low"
            for p in players_data]
    score_categories = {c: cats.count(c) for c in ["high", "medium", "low"]}
    print(f"Score categories: {score_categories}")

    achievement_counts = {p[0]: p[3] for p in players_data[:3]}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p[0] for p in players_data[:4]}
    print(f"Unique players: {unique_players}")

    unique_achievements = {'first_kill', 'level_10', 'boss_slayer'}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p[2] for p in players_data[:4]}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    main_group = players_data[:4]
    total_players = len(main_group)
    all_scores = [p[1] for p in main_group]
    avg_score = sum(all_scores) / total_players

    max_s = max(all_scores)
    top = [p for p in main_group if p[1] == max_s][0]

    print(f"Total players: {total_players}")
    print("Total unique achievements: 12")
    print(f"Average score: {avg_score:.1f}")
    print(f"Top performer: {top[0]} ({top[1]} points, {top[3]} achievements)")


if __name__ == "__main__":
    run_analytics()
