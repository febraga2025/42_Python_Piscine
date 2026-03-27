from ex3.CardFactory import CardFactory
from ex0.Card import Card, CardRarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, SpellEffect


class FantasyCardFactory(CardFactory):
    def __init__(self):
        # Suporte extensível: guardamos as "receitas" das cartas em dicionários
        self._creatures = {
            "dragon": ("Fire Dragon", 5, CardRarity.LEGENDARY, 7, 10),
            "goblin": ("Goblin Warrior", 2, CardRarity.COMMON, 2, 2)
        }
        self._spells = {
            "fireball": ("Fireball", 3, CardRarity.RARE, SpellEffect.DAMAGE, "Causa dano de fogo")
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Cria criaturas temáticas de fantasia."""
        name = str(name_or_power).lower() if name_or_power else "goblin"
        
        if name in self._creatures:
            args = self._creatures[name]
            return CreatureCard(*args)
        
        # Caso não encontre, retorna uma criatura padrão (ou levanta erro)
        return CreatureCard("Mysterious Beast", 3, CardRarity.COMMON, 3, 3)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Cria feitiços elementais."""
        name = str(name_or_power).lower() if name_or_power else "fireball"
        
        if name in self._spells:
            args = self._spells[name]
            return SpellCard(*args)
        
        return SpellCard("Magic Spark", 1, CardRarity.COMMON, SpellEffect.DAMAGE, "Um pequeno brilho")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Cria artefatos mágicos (ex: anéis, cajados)."""
        # Implementação similar usando sua classe ArtifactCard
        # Para o exemplo do PDF, vamos retornar algo básico
        return CreatureCard("Mana Ring", 1, CardRarity.RARE, 0, 1)

    def create_themed_deck(self, size: int) -> dict:
        """Gera um deck completo misturando os tipos."""
        deck = []
        for i in range(size):
            if i % 3 == 0:
                deck.append(self.create_creature("dragon" if i == 0 else "goblin"))
            elif i % 3 == 1:
                deck.append(self.create_spell("fireball"))
            else:
                deck.append(self.create_artifact())
        
        return {
            "theme": "Fantasy",
            "size": len(deck),
            "cards": [card.name for card in deck]
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
        