import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if len(args) >= 3 and hasattr(args[0], 'cast_spell'):
                power = args[2]
            else:
                power = args[0] if args else kwargs.get('power', 0)

            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    test_powers = [13, 25, 7, 13]
    spell_names = ['flash', 'earthquake', 'tornado', 'freeze']
    invalid_names = ['Jo', 'A', 'Alex123']

    guild = MageGuild()

    print("Testing spell timer...")

    @spell_timer
    def flash_spell():
        time.sleep(0.101)
        return "Fireball cast!"

    res = flash_spell()
    print(f"Result: {res}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell():
        raise Exception("Mana Leak")

    print(unstable_spell())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Casey"))
    print(MageGuild.validate_mage_name(invalid_names[0]))

    print(guild.cast_spell(spell_names[1], test_powers[1]))
    print(guild.cast_spell(spell_names[2], test_powers[2]))
