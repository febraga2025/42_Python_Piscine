try:
    from alchemy.grimoire import (validate_ingredients, record_spell)

except ImportError as e:
    print(f"Import Error: {e}")


def test_circular_curse():
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    test_cases = ["fire air", "dragon scales"]
    for ingredients in test_cases:
        res = validate_ingredients(ingredients)
        print(f'validate_ingredients("{ingredients}"): {res}')

    print("\nTesting spell recording with validation:")
    spells = [("Fireball", "fire air"), ("Dark Magic", "shadow")]
    for name, ing in spells:
        print(f'record_spell("{name}", "{ing}"): {record_spell(name, ing)}')

    print("\nTesting late import technique:")
    print('record_spell("Lightning", "air"):'
          f' {record_spell("Lightning", "air")}')

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    test_circular_curse()
