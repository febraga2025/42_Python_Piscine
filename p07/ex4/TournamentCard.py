from ex0.Card import Card, CardRarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict, Any


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str, cost: int, rarity: CardRarity,
                 attack: int, health: int, initial_rating: int = 1000):
        super().__init__(name, cost, rarity)

        self.card_id = card_id
        self.attack_power = attack
        self.health = health
        self.rating = initial_rating
        self.wins = 0
        self.losses = 0

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += (wins * 16)

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating = max(0, self.rating - (losses * 16))

    def get_rank_info(self) -> Dict[str, Any]:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
        }

    def play(self, game_state: dict) -> Dict[str, Any]:
        return {"action": "Tournament play", "card": self.name}

    def attack(self, target: str) -> Dict[str, Any]:
        return {"attacker": self.name, "damage": self.attack_power}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        self.health -= incoming_damage
        return {"defender": self.name, "health_left": self.health}

    def get_combat_stats(self) -> Dict[str, int]:
        return {"attack": self.attack_power, "health": self.health}
