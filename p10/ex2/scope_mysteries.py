from typing import Any
from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchanter


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    initial_powers = [63, 80, 48]
    power_additions = [15, 20, 19, 11, 16]
    enchantment_types = ['Shocking', 'Dark', 'Flowing']
    items_to_enchant = ['Wand', 'Ring', 'Cloak', 'Shield']

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = initial_powers[0]
    acc = spell_accumulator(base)

    add1 = power_additions[0]
    add2 = power_additions[1]
    print(f"Base {base}, add {add1}: {acc(add1)}")
    print(f"Base {base}, add {add2}: {acc(add2)}")

    print("Testing enchantment factory...")
    factory1 = enchantment_factory(enchantment_types[0])
    factory2 = enchantment_factory(enchantment_types[1])

    print(factory1(items_to_enchant[0]))
    print(factory2(items_to_enchant[1]))

    print("Testing memory vault...")
    v = memory_vault()
    key = "secret"
    val = initial_powers[2]
    print(f"Store '{key}' = {val}")
    v["store"](key, val)
    print(f"Recall '{key}': {v['recall'](key)}")
    print(f"Recall 'unknown': {v['recall']('unknown')}")
