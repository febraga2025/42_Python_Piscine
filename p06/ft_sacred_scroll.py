import alchemy
import alchemy.elements


def test_sacred_scroll() -> None:
    print("Sacred Scroll Mastery")

    print("\nTesting direct module access:")
    print(
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(
        f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    for spell in ["create_earth", "create_air"]:
        try:
            func = getattr(alchemy, spell)
            print(f"alchemy.{spell}(): {func()}")
        except AttributeError:
            print(f"alchemy.{spell}(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    test_sacred_scroll()
