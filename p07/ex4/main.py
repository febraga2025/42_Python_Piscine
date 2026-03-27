from ex0.Card import CardRarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

def main():
    print("=== DataDeck Tournament Platform ===")
    
    # 1. Inicializando a Plataforma
    platform = TournamentPlatform()
    
    # 2. Criando as cartas de torneio
    # Nota: Usamos os valores que levam ao ELO esperado (Ataque maior ganha)
    dragon = TournamentCard(
        card_id="dragon_001", 
        name="Fire Dragon", 
        cost=5, 
        rarity=CardRarity.LEGENDARY, 
        attack=10, 
        health=10, 
        initial_rating=1200
    )
    
    wizard = TournamentCard(
        card_id="wizard_001", 
        name="Ice Wizard", 
        cost=4, 
        rarity=CardRarity.RARE, 
        attack=7, 
        health=8, 
        initial_rating=1150
    )

    print("Registering Tournament Cards...")
    platform.register_card(dragon)
    platform.register_card(wizard)

    # Exibindo informações iniciais das cartas
    for card in [dragon, wizard]:
        rank = card.get_rank_info()
        print(f"{card.name} (ID: {card.card_id}):")
        # Mostrando a herança múltipla em ação
        print(f"- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {rank['rating']}")
        print(f"- Record: {rank['record']}")

    # 3. Executando a partida
    print("\nCreating tournament match...")
    match_result = platform.run_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    # 4. Exibindo o Leaderboard (Placar)
    print("\nTournament Leaderboard:")
    # Ordenamos por rating (do maior para o menor)
    sorted_cards = sorted(platform.registry.values(), key=lambda c: c.rating, reverse=True)
    for i, card in enumerate(sorted_cards, 1):
        rank = card.get_rank_info()
        print(f"{i}. {card.name} - Rating: {rank['rating']} ({rank['record']})")

    # 5. Relatório Final
    print("\nPlatform Report:")
    print(platform.get_platform_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously")

if __name__ == "__main__":
    main()