class TournamentPlatform:
    def __init__(self):
        self.registry = {} # Guarda as cartas por ID
        self.matches_played = 0

    def register_card(self, card):
        self.registry[card.card_id] = card

    def run_match(self, player1_id: str, player2_id: str) -> dict:
        p1 = self.registry[player1_id]
        p2 = self.registry[player2_id]
        
        # Lógica de vitória: quem tem mais ataque ganha (simples para o exemplo)
        p1_wins = p1.attack_power >= p2.attack_power
        
        # Armazena ratings antigos para o cálculo
        r1, r2 = p1.rating, p2.rating
        
        # Atualiza ambos os ratings
        p1.update_rating(r2, p1_wins)
        p2.update_rating(r1, not p1_wins)
        
        self.matches_played += 1
        
        return {
            "winner": p1.card_id if p1_wins else p2.card_id,
            "loser": p2.card_id if p1_wins else p1.card_id,
            "winner_rating": p1.rating if p1_wins else p2.rating,
            "loser_rating": p2.rating if p1_wins else p1.rating
        }

    def get_platform_report(self) -> dict:
        ratings = [c.rating for c in self.registry.values()]
        return {
            "total_cards": len(self.registry),
            "matches_played": self.matches_played,
            "avg_rating": sum(ratings) // len(ratings) if ratings else 0,
            "platform_status": "active"
        }