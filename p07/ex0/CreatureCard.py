from ex0.Card import Card, CardRarity


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: CardRarity,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name if hasattr(target, 'name') else target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
