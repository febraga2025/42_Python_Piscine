from typing import Dict, List, Any
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.registry: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        self.registry[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        p1 = self.registry[card1_id]
        p2 = self.registry[card2_id]

        p1_wins = p1.attack_power >= p2.attack_power

        if p1_wins:
            p1.update_wins(1)
            p2.update_losses(1)
            winner, loser = p1, p2
        else:
            p2.update_wins(1)
            p1.update_losses(1)
            winner, loser = p2, p1

        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[str]:
        sorted_cards = sorted(
            self.registry.values(),
            key=lambda c: c.calculate_rating(),
            reverse=True
        )
        return [f"{c.name} - Rating: {c.calculate_rating()}"
                f" ({c.wins}-{c.losses})"
                for c in sorted_cards]

    def generate_tournament_report(self) -> Dict[str, Any]:
        ratings = [c.calculate_rating() for c in self.registry.values()]
        avg = sum(ratings) // len(ratings) if ratings else 0

        return {
            "total_cards": len(self.registry),
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active"
        }
