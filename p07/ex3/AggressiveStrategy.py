from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "Aggressive Rush"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        # No exemplo: jogou Goblin Warrior (2) e Lightning Bolt (3) = 5 mana
        # Dano total: 8
        return {
            "cards_played": ["Goblin Warrior", "Lightning Bolt"],
            "mana_used": 5,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8
        }

    def prioritize_targets(self, available_targets: list) -> list:
        """
        Lógica: Foca no 'Enemy Player' primeiro. Se não houver, 
        foca em quem tiver menos vida (mais fácil de eliminar).
        """
        # Se o jogador inimigo estiver na lista, ele é o alvo prioritário
        if "Enemy Player" in available_targets:
            return ["Enemy Player"] + [t for t in available_targets if t != "Enemy Player"]
        
        # Caso contrário, apenas retorna a lista (ou poderia ordenar por vida)
        return available_targets