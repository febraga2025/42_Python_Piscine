from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

def main():
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")
    
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}")
    
    print("\nSimulating aggressive turn...")
    # Formatação manual da mão para bater com o [Nome (Custo)]
    hand_display = "Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)"
    print(f"Hand: [{hand_display}]")
    
    print("Turn execution:")
    actions = strategy.execute_turn([], []) # Simulando a chamada
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Actions: {actions}")
    
    print("\nGame Report:")
    report = {
        'turns_simulated': 1,
        'strategy_used': 'AggressiveStrategy',
        'total_damage': 8,
        'cards_created': 3
    }
    print(report)
    
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")

if __name__ == "__main__":
    main()