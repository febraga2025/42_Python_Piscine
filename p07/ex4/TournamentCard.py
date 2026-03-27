from ex0.Card import Card, CardRarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

# Herança Múltipla: TournamentCard é um Card, é Combatable e é Rankable
class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str, cost: int, rarity: CardRarity, 
                 attack: int, health: int, initial_rating: int = 1000):
        # Inicializa a base (Card)
        super().__init__(name, cost, rarity)
        
        # Atributos específicos do torneio
        self.card_id = card_id
        self.attack_power = attack
        self.health = health
        self.rating = initial_rating
        self.wins = 0
        self.losses = 0

    def update_rating(self, opponent_rating: int, won: bool) -> int:
        k_factor = 32 
        
        expected_win_probability = self.rating / (self.rating + opponent_rating)
        
        actual_result = 1 if won else 0
        
        rating_change = round(k_factor * (actual_result - expected_win_probability))
        
        self.rating += rating_change
        
        if won:
            self.wins += 1
        else:
            self.losses += 1
            
        return self.rating

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    # --- Métodos obrigatórios das interfaces anteriores ---
    def play(self, game_state: dict) -> dict:
        return {"action": "Tournament play", "card": self.name}

    def attack(self, target: str) -> dict:
        return {"attacker": self.name, "damage": self.attack_power}

    def defend(self, damage: int) -> dict:
        self.health -= damage
        return {"defender": self.name, "health_left": self.health}

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power, "health": self.health}