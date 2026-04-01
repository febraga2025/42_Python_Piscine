from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    hand_display = "Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)"
    print(f"Hand: [{hand_display}]\n")

    print("Turn execution:")
    actions = engine.simulate_turn()
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Actions: {actions}")

    print("\nGame Report:")
    report = engine.get_engine_status()
    print(report)

    print("\nAbstract Factory + Strategy Pattern:"
          " Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
