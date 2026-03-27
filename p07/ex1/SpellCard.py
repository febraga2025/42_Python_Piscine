from ex0.Card import Card, CardRarity
from enum import Enum

class SpellEffect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: CardRarity, effect_type: str,
                 effect_description: str):
        super().__init__(name, cost, rarity)
        if not isinstance(effect_type, SpellEffect):
            raise TypeError("effect_type must be a SpellEffect Enum member")
        self.effect_type = effect_type
        self.effect_description = effect_description

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_description}

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["effect_type"] = self.effect_type.value
        return info

    def resolve_effect(self, target) -> dict:
        target_name = target.name if hasattr(target, 'name') else target
        return {
            "spell": self.name,
            "effect": self.effect_type.value,
            "target": target_name,
            "status": "Effect resolved"
        }
