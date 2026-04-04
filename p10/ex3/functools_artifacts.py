import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(ops[operation], spells)


def base_enchant(power: int, element: str, target: str) -> str:
    return f"Casting {element} spell (Power: {power}) on {target}"


def partial_enchanter(base_func: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": functools.partial(base_func, 50, "Fire"),
        "ice_enchant": functools.partial(base_func, 50, "Ice"),
        "lightning_enchant": functools.partial(base_func, 50, "Lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@functools.singledispatch
def spell_dispatcher(arg: Any):
    return "Unknown magical essence"


@spell_dispatcher.register(int)
def _(arg: int):
    return f"Damage spell: {arg} HP"


@spell_dispatcher.register(str)
def _(arg: str):
    return f"Enchantment: {arg}"


@spell_dispatcher.register(list)
def _(arg: list):
    return f"Multi-cast: {len(arg)} spells"


if __name__ == "__main__":
    spell_powers = [48, 49, 34, 23, 47, 22]
    operations = ['add', 'multiply', 'max', 'min']
    fib_tests = [10, 17, 20]

    print("=== Testing Spell Reducer ===")
    print(f"Sum (add): {spell_reducer(spell_powers, 'add')}")
    print(f"Max value: {spell_reducer(spell_powers, 'max')}")

    print("\n=== Testing Partial Enchanter ===")
    enchanters = partial_enchanter(base_enchant)
    print(enchanters["fire_enchant"]("Iron Shield"))
    print(enchanters["lightning_enchant"]("Silver Sword"))

    print("\n=== Testing Memoized Fibonacci ===")
    for n in fib_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    print("\n=== Testing Spell Dispatcher ===")
    print(spell_dispatcher(100))
    print(spell_dispatcher("Invisibility"))
    print(spell_dispatcher([48, 49, 34]))
