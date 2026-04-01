from ex0.Card import Card, CardRarity
from enum import Enum


class SpellEffect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: CardRarity,
                 effect_type: str, effect_description: str):
        super().__init__(name, cost, rarity)
        valid_effects = [e.value for e in SpellEffect]
        if effect_type not in valid_effects:
            raise ValueError(f"effect_type must be one of {valid_effects}")
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
