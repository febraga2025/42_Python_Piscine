from ex0.Card import CardRarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("dragon_001", "Fire Dragon", 5,
                            CardRarity.LEGENDARY, 10, 15, 1200)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4,
                            CardRarity.RARE, 7, 10, 1150)

    print("Registering Tournament Cards...")
    platform.register_card(dragon)
    platform.register_card(wizard)

    for card in [dragon, wizard]:
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    sorted_cards = sorted(platform.registry.values(),
                          key=lambda c: c.calculate_rating(), reverse=True)

    for i, card in enumerate(sorted_cards, 1):
        print(f"{i}. {card.name} - Rating: {card.calculate_rating()} "
              f"({card.wins}-{card.losses})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
