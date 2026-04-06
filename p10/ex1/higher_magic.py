from collections.abc import Callable
from typing import Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> Any:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> Any:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [s(target, power) for s in spells]
    return sequence


if __name__ == "__main__":
    test_values = [6, 17, 14]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def is_dragon(target: str, _power: int) -> bool:
        return target == "Dragon"

    print("=== Testing Spell Combiner ===")
    combo = spell_combiner(fireball, heal)
    print(f"Target {test_targets[3]}: {combo(test_targets[3], 10)}")

    print("\n=== Testing Power Amplifier ===")
    multiplier = test_values[0]
    mega_fire = power_amplifier(fireball, multiplier)
    print(f"Multiplier {multiplier}x | Power 10 -> "
          f"{mega_fire(test_targets[1], 10)}")

    print("\n=== Testing Conditional Caster ===")
    dragon_slayer = conditional_caster(is_dragon, fireball)
    print(f"Target {test_targets[0]}: {dragon_slayer(test_targets[0], 50)}")
    print(f"Target {test_targets[2]}: {dragon_slayer(test_targets[2], 50)}")

    print("\n=== Testing Spell Sequence ===")
    ritual = spell_sequence([fireball, heal])
    print(f"Sequence on {test_targets[2]}:")
    results = ritual(test_targets[2], 15)
    for res in results:
        print(f"  - {res}")
