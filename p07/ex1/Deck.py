import random
from typing import List, Dict
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        if not self._cards:
            raise IndexError("The deck is empty! There's nothing to draw.")
        return self._cards.pop(0)

    def get_deck_stats(self) -> Dict[str, any]:
        total = len(self._cards)
        if total == 0:
            return {"total_cards": 0, "creatures": 0, "spells": 0,
                    "artifacts": 0, "avg_cost": 0.0}
        total_mana_cost = sum(card.cost for card in self._cards)
        avg_cost = total_mana_cost / total

        creatures = sum(1 for c in self._cards
                        if c.__class__.__name__ == "CreatureCard")
        spells = sum(1 for c in self._cards
                     if c.__class__.__name__ == "SpellCard")
        artifacts = sum(1 for c in self._cards
                        if c.__class__.__name__ == "ArtifactCard")

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 2)}
