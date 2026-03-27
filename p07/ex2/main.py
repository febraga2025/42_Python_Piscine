from ex0.Card import Card, CardRarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")

    card_order = ['play', 'get_card_info', 'is_playable']
    combat_order = ['attack', 'defend', 'get_combat_stats']
    magic_order = ['cast_spell', 'channel_mana', 'get_magic_stats']

    print("EliteCard capabilities:")
    methods_card = [m for m in card_order if hasattr(Card, m)]
    methods_combat = [m for m in combat_order if hasattr(Combatable, m)]
    methods_magic = [m for m in magic_order if hasattr(Magical, m)]

    print(f"- Card: {methods_card}")
    print(f"- Combatable: {methods_combat}")
    print(f"- Magical: {methods_magic}")

    warrior = EliteCard("Arcane Warrior", 5, CardRarity.RARE, 5, 10)
    print(f"\nPlaying {warrior.name} (Elite Card):")

    print("Combat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    print(
        f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
