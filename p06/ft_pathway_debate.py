try:
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    from alchemy.transmutation.advanced import (philosophers_stone,
                                                elixir_of_life)
except ImportError as e:
    print(f"Error preparing pathways: {e}")
import alchemy.transmutation


def main():
    print("=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    try:
        print(f"lead_to_gold(): {lead_to_gold()}")
        print(f"stone_to_gem(): {stone_to_gem()}")
    except Exception as e:
        print(f"Error: Absolute path execution failure: {e}")

    print("\nTesting Relative Imports (from advanced.py):")
    try:
        print(f"philosophers_stone(): {philosophers_stone()}")
        print(f"elixir_of_life(): {elixir_of_life()}")
    except Exception as e:
        print(f"Error: Relative path execution failure: {e}")

    print("\nTesting Package Access:")
    try:
        print(f"alchemy.transmutation.lead_to_gold(): "
              f"{alchemy.transmutation.lead_to_gold()}")
    except Exception as e:
        print(f"Error:Package Access error: {e}")

    try:
        print(f"alchemy.transmutation.philosophers_stone(): "
              f"{alchemy.transmutation.philosophers_stone()}")
    except Exception as e:
        print(f"Error:Package Access error: {e}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
