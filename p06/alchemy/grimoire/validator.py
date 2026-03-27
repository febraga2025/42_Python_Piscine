def validate_ingredients(ingredients: str) -> str:
    holy_elements = ["fire", "water", "earth", "air"]

    if any(element in ingredients.lower() for element in holy_elements):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
