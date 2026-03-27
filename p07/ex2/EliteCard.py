from ex0.Card import Card, CardRarity
from ex1.SpellCard import SpellEffect # Importamos o Enum de efeitos do Ex 1
from ex2.Combatable import Combatable
from ex2.Magical import Magical

class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: CardRarity, 
                 attack: int, mana_pool: int):
        super().__init__(name, cost, rarity)
        
        self.attack_power = attack
        self.mana = mana_pool
        self.health = 10

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError("Damage must be a non-negative integer")
        
        damage_blocked = 3
        actual_damage = max(0, incoming_damage - damage_blocked)
        self.health -= actual_damage
        return {
            "defender": self.name,
            "damage_taken": actual_damage,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = 4
        self.mana -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "rarity": self.rarity.value,
            "status": "Elite Warrior enters the fray"
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    def channel_mana(self, amount: int) -> dict:
        if amount < 0:
            raise ValueError("Mana amount must be positive")
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana
        }