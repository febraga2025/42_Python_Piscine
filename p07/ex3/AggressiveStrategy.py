from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "Aggressive Rush"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        _ = hand
        _ = battlefield
        return {
            "cards_played": ["Goblin Warrior", "Lightning Bolt"],
            "mana_used": 5,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8
        }

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            return (["Enemy Player"] +
                    [t for t in available_targets if t != "Enemy Player"])

        return available_targets
