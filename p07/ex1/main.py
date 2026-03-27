from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    my_deck = Deck()
    list_card = [
        SpellCard("Lightning Bolt", 3, "Common", "damage",
                  "Deal 3 damage to target"),
        ArtifactCard("Mana Crystal", 2, "Common", 5,
                     "Permanent: +1 mana per turn"),
        CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)]
    for c in list_card:
        my_deck.add_card(c)

    stats = my_deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:")

    for _ in range(stats['total_cards']):
        card = my_deck.draw_card()
        card_type = card.__class__.__name__.replace("Card", "")
        print(f"Drew: {card.name} ({card_type})")
        print(f"Play result: {card.play({})}\n")

    print("\nPolymorphism in action: Same"
          "interface, different card behaviors!")


if __name__ == "__main__":
    main()
