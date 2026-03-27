from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    try:
        fire = create_fire()
        return f"Lead transmuted to gold using {fire}"
    except Exception as e:
        return f"Absolute transmutation error: {e}"


def stone_to_gem() -> str:
    try:
        earth = create_earth()
        return f"Stone transmuted to gem using {earth}"
    except Exception as e:
        return f"Absolute transmutation error: {e}"
