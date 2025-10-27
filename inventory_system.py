"""Inventory management system with stock tracking and logging."""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item: Item name (default: "default")
        qty: Quantity to add (default: 0)
        logs: List to store log messages (default: None)

    Returns:
        None
    """
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str):
        print(f"Error: Item name must be a string, got {type(item).__name__}")
        return
    if not isinstance(qty, (int, float)):
        print(f"Error: Quantity must be a number, got {type(qty).__name__}")
        return
    if not item:
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove an item from the inventory.

    Args:
        item: Item name to remove
        qty: Quantity to remove

    Returns:
        None
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass  # Item not found in inventory


def get_qty(item):
    """
    Get the quantity of an item in inventory.

    Args:
        item: Item name to query

    Returns:
        Quantity of the item
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file: Path to the JSON file (default: "inventory.json")

    Returns:
        None
    """
    with open(file, "r", encoding="utf-8") as f:
        global stock_data
        stock_data = json.loads(f.read())


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file: Path to the JSON file (default: "inventory.json")

    Returns:
        None
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def print_data():
    """
    Print the current inventory report.

    Returns:
        None
    """
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """
    Check for items below a certain threshold.

    Args:
        threshold: Minimum quantity threshold (default: 5)

    Returns:
        List of items below the threshold
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """
    Main function to demonstrate inventory system operations.

    Returns:
        None
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print('eval used')  # Removed dangerous eval()


main()