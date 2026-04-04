from typing import Callable, Any


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

    print("=== Testing Mage Counter ===")
    counter_spell = mage_counter()
    print(f"Call 1: {counter_spell()}")
    print(f"Call 2: {counter_spell()}")

    print("\n=== Testing Spell Accumulator ===")
    acc = spell_accumulator(initial_powers[0])
    print(f"Initial 63 + {power_additions[0]} = {acc(power_additions[0])}")
    print(f"Total + {power_additions[1]} = {acc(power_additions[1])}")

    print("\n=== Testing Enchantment Factory ===")
    shock_factory = enchantment_factory(enchantment_types[0])
    print(shock_factory(items_to_enchant[0]))
    print(shock_factory(items_to_enchant[1]))

    print("\n=== Testing Memory Vault ===")
    vault = memory_vault()
    vault["store"]("secret_spell", "Abra Kadabra")
    print(f"Recalling secret: {vault['recall']('secret_spell')}")
    print(f"Recalling ghost: {vault['recall']('non_existent')}")
