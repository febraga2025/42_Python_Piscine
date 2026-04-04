import functools
import time
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args and not isinstance(args[0], (int, float)):
                power = args[1]
            else:
                power = args[0]

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
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    test_powers = [5, 15, 25]
    spell_names = ["fireball", "heal"]
    invalid_names = ['Jo', 'A', 'Alex123']

    guild = MageGuild()

    print("=== Testing Power Validator via MageGuild ===")
    print(guild.cast_spell(test_powers[0], spell_names[0]))
    print(guild.cast_spell(test_powers[1], spell_names[1]))

    print("\n== Testing Static Method (Name Validation) ===")
    for name in invalid_names:
        print(f"Is '{name}' valid? {MageGuild.validate_mage_name(name)}")

    print("\n=== Testing Spell Timer ===")

    @spell_timer
    def slow_spell():
        time.sleep(0.1)
        return "Done!"
    slow_spell()
