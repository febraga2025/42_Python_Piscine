
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))
    if not powers:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    max_p = max(powers)
    min_p = min(powers)
    avg_p = round(sum(powers) / len(powers), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


if __name__ == "__main__":

    artifacts = [{'name': 'Water Chalice', 'power': 91, 'type': 'focus'},
                 {'name': 'Lightning Rod', 'power': 87, 'type': 'relic'},
                 {'name': 'Light Prism', 'power': 76, 'type': 'weapon'},
                 {'name': 'Earth Shield', 'power': 103, 'type': 'accessory'}
                 ]
    mages = [
        {'name': 'Zara', 'power': 61, 'element': 'earth'},
        {'name': 'Storm', 'power': 99, 'element': 'lightning'},
        {'name': 'Storm', 'power': 70, 'element': 'wind'},
        {'name': 'Riley', 'power': 79, 'element': 'wind'},
        {'name': 'Nova', 'power': 78, 'element': 'earth'}
        ]

    spells = ['tsunami', 'blizzard', 'fireball', 'tornado']

    print("=== Ordered Artifacts (power desc) ===")
    print(artifact_sorter(artifacts))

    print("\n=== Mages With Power >= 80 ===")
    print(power_filter(mages, 80))

    print("\n=== Transformer Spells ===")
    print(spell_transformer(spells))

    print("\n===Mages Statistic ===")
    print(mage_stats(mages))
