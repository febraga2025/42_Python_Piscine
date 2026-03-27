from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    try:
        gold = lead_to_gold()
        potion = healing_potion()
        return (
            f"Philosopher's stone created using {gold} "
            f"and {potion}")
    except Exception as e:
        return f"Relative transmutation error: {e}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
