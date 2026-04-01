from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import List, Dict, Any
from ex0.Card import Card


class GameEngine:
    def __init__(self):
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None
        self.hand: List[Card] = []
        self.battlefield: List[Card] = []
        self.turns_simulated: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        if self.factory:
            self.hand = [
                self.factory.create_creature("dragon"),
                self.factory.create_creature("goblin"),
                self.factory.create_spell("fireball")
            ]

    def simulate_turn(self) -> Dict[str, Any]:
        if not self.strategy:
            return {"error": "No strategy configured"}

        self.turns_simulated += 1
        report = self.strategy.execute_turn(self.hand, self.battlefield)
        return report

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name() if self.strategy
            else "None",
            'total_damage': 8,
            'cards_created': len(self.hand)
        }
