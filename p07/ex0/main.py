from ex0.CreatureCard import CreatureCard, CardRarity


def main():
    print("=== DataDeck Card Foundation ==")
    print("\nTesting Abstract Base Class Design:")
    try:
        fire_dragon = CreatureCard(
            name="Fire Dragon",
            cost=5,
            rarity=CardRarity.LEGENDARY,
            attack=7,
            health=5
        )
        goblin = CreatureCard("Goblin Warrior", 2, CardRarity.COMMON, 2, 2)

        print("\nCreatureCard info:")
        print(fire_dragon.get_card_info())

        mana_available = 6
        print(f"\nPlaying {fire_dragon.name} with {mana_available}"
              " mana available:")
        print(f"Playable: {fire_dragon.is_playable(mana_available)}")
        print(f"Play result: {fire_dragon.play({})}")

        print(f"\n{fire_dragon.name} attacks {goblin.name}:")
        attack_result = fire_dragon.attack_target(goblin)
        print(f"Attack result: {attack_result}")

        mana_low = 3
        print(f"\nTesting insufficient mana ({mana_low} available):")
        print(f"Playable: {fire_dragon.is_playable(mana_low)}")

        print("\nAbstract pattern successfully demonstrated!")

    except Exception as e:
        print(f"An alchemical error occurred: {e}")


if __name__ == "__main__":
    main()
