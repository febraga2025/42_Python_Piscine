import sys


def get_inventory() -> dict[str, dict]:
    catalog = {
        'sword': {'type': 'weapon', 'price': 150},
        'sclearhield': {'type': 'armor', 'price': 200},
        'potion': {'type': 'consumable', 'price': 25},
        'crystal': {'type': 'material', 'price': 1000}
    }

    inventory = {}
    for arg in sys.argv[1:]:
        if ":" not in arg:
            continue
        try:
            name, qty_str = arg.split(":")
            qty = int(qty_str)

            item_info = catalog.get(name, {'type': 'misc', 'price': 10})

            item_data = {
                "name": name,
                "type": item_info['type'],
                "quantity": qty,
                "value": qty * item_info['price']
            }

            inventory.update({name: item_data})
        except ValueError:
            continue
    return inventory


def main() -> None:
    """Core logic demonstrating nested dicts and required methods."""
    inventory = get_inventory()
    if not inventory:
        print("Usage: python3 ft_inventory_system.py item:qty ...")
        return

    total_units = 0
    for data in inventory.values():
        total_units += data["quantity"]

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_units}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for name, data in inventory.items():
        qty = data["quantity"]
        perc = (qty / total_units) * 100 if total_units > 0 else 0
        label = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {label} ({perc:.1f}%)")

    most_abundant = None
    least_abundant = None

    for name in inventory.keys():
        curr_qty = inventory[name]["quantity"]
        if most_abundant is None or curr_qty > inventory[most_abundant]["q"]:
            pass

    for name in inventory.keys():
        q_now = inventory[name]["quantity"]
        if (most_abundant is None or
                q_now > inventory[most_abundant]["quantity"]):
            most_abundant = name
        if (least_abundant is None or
                q_now < inventory[least_abundant]["quantity"]):
            least_abundant = name

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} "
          f"({inventory[most_abundant]['quantity']} units)")
    print(f"Least abundant: {least_abundant} "
          f"({inventory[least_abundant]['quantity']} units)")

    moderate = {}
    scarce = {}
    for name, data in inventory.items():
        if data["quantity"] >= 4:
            moderate[name] = data["quantity"]
        else:
            scarce[name] = data["quantity"]

    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = [n for n, d in inventory.items() if d.get("quantity", 0) <= 1]
    print(f"Restock needed: {', '.join(restock) if restock else 'None'}")

    print("\n=== Dictionary Properties Demo ===")
    keys_str = ", ".join(inventory.keys())
    values_list = [str(data["quantity"]) for data in inventory.values()]
    values_str = ", ".join(values_list)
    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {values_str}")
    has_sword = "sword" in inventory
    print(f"Sample lookup - 'sword' in inventory: {has_sword}")


if __name__ == "__main__":
    main()
