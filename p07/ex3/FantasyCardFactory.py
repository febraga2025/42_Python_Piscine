from ex3.CardFactory import CardFactory
from ex0.Card import Card, CardRarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict, Any


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creatures = {
            "dragon": ("Fire Dragon", 5, CardRarity.LEGENDARY, 7, 10),
            "goblin": ("Goblin Warrior", 2, CardRarity.COMMON, 2, 2)
        }
        self._spells = {
            "fireball": ("Fireball", 3, CardRarity.RARE, "damage",
                         "Deal 3 damage to target")
        }
        self._artifacts = {
            "mana_ring": ("Mana Ring", 2, CardRarity.RARE, 5,
                          "Permanent: +1 mana per turn")
        }

    def create_creature(self, name: str | None = None) -> Card:
        key = name.lower() if name else "goblin"
        if key in self._creatures:
            return CreatureCard(*self._creatures[key])
        return CreatureCard("Mysterious Beast", 3, CardRarity.COMMON, 3, 3)

    def create_spell(self, name: str | None = None) -> Card:
        key = name.lower() if name else "fireball"
        if key in self._spells:
            return SpellCard(*self._spells[key])
        return SpellCard("Magic Spark", 1, CardRarity.COMMON, "damage",
                         "Small spark")

    def create_artifact(self, name: str | None = None) -> Card:
        key = name.lower() if name else "mana_ring"
        if key in self._artifacts:
            return ArtifactCard(*self._artifacts[key])
        return ArtifactCard("Old Relic", 1, CardRarity.COMMON, 1, "No effect")

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        deck = []
        for i in range(size):
            if i % 3 == 0:
                deck.append(self.create_creature("dragon" if i == 0 else
                                                 "goblin"))
            elif i % 3 == 1:
                deck.append(self.create_spell("fireball"))
            else:
                deck.append(self.create_artifact())
        return {"theme": "Fantasy", "cards": [c.name for c in deck]}

    def get_supported_types(self) -> Dict[str, list]:
        return {
            'creatures': list(self._creatures.keys()),
            'spells': list(self._spells.keys()),
            'artifacts': list(self._artifacts.keys())
        }
