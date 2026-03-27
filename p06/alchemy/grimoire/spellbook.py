def record_spell(spell_name: str, ingredients: str) -> str:
    try:
        from .validator import validate_ingredients

        status = validate_ingredients(ingredients)

        if "INVALID" in status:
            return f"Spell rejected: {spell_name} ({status})"
        return f"Spell recorded: {spell_name} ({status})"

    except Exception as e:
        return f"Grimoire Error: {str(e)}"
