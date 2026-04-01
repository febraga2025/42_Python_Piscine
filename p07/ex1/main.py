from ex0.Card import CardRarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===\n")
    deck = Deck()

    print("Building deck with different card types...")

    bolt = SpellCard("Lightning Bolt", 3, CardRarity.COMMON, "damage",
                     "Deal 3 damage to target")
    crystal = ArtifactCard("Mana Crystal", 2, CardRarity.RARE, 4,
                           "Permanent: +1 mana per turn")
    dragon = CreatureCard("Fire Dragon", 7, CardRarity.LEGENDARY, 7, 10)

    for card in [bolt, crystal, dragon]:
        deck.add_card(card)

    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")
    for card in [bolt, crystal, dragon]:
        card_type = card.__class__.__name__.replace('Card', '')
        print(f"Drew: {card.name} ({card_type})")
        print(f"Play result: {card.play({})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
