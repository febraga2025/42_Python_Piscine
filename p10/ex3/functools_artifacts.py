import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        return 0

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
    """Calcula Fibonacci com cache para alta performance."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatcher.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatcher.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatcher


if __name__ == "__main__":
    spell_powers = [48, 49, 34, 23, 47, 22]
    fib_tests = [10, 15]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    print("\nTesting memoized fibonacci...")
    for n in [0, 1] + fib_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))
