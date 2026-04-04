from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args: Any, **kwargs: Any) -> tuple:
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args: Any, **kwargs: Any) -> int | float:
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args: Any, **kwargs: Any) -> list:
        return [s(*args, **kwargs) for s in spells]
    return sequence


if __name__ == "__main__":
    test_values = [16, 5, 12]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def basic_damage(target: str) -> int:
        return 10

    def is_dragon(target: str) -> bool:
        return target == "Dragon"

    print("=== Testing Spell Combiner ---")
    combo = spell_combiner(fireball, heal)
    print(combo(test_targets[0]))

    print("\n=== Testing Power Amplifier ===")
    mega_damage = power_amplifier(basic_damage, test_values[0])
    print(f"Damage to {test_targets[1]}: {mega_damage(test_targets[1])}")

    print("\n=== Testing Conditional Caster ===")
    dragon_slayer = conditional_caster(is_dragon, fireball)
    print(f"Target Dragon: {dragon_slayer('Dragon')}")
    print(f"Target Goblin: {dragon_slayer('Goblin')}")

    print("\n=== Testing Spell Sequence ===")
    ritual = spell_sequence([fireball, heal])
    print(ritual(test_targets[2]))
