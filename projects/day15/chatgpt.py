MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def report(resources_data):
    """Print the current resources of the coffee machine."""
    print(f"\nResource Report:")
    print(f"Water: {resources_data.get('water', 0)} mL")
    print(f"Milk: {resources_data.get('milk', 0)} mL")
    print(f"Coffee: {resources_data.get('coffee', 0)} g")
    print(f"Money: ${resources_data.get('money', 0):.2f}\n")

def check_resources(order_name, available_resources):
    """Check if resources are sufficient for the order."""
    missing = []
    required_ingredients = MENU[order_name]["ingredients"]
    for item, amount_needed in required_ingredients.items():
        if available_resources.get(item, 0) < amount_needed:
            missing.append(item)
    return missing

def get_user_coins():
    """Prompt user to insert coins and return as a dictionary."""
    print("Please insert coins:")
    return {coin: int(input(f"How many {coin}?: ")) for coin in COINS}

def process_coins(coin_input):
    """Calculate the total money from inserted coins."""
    return sum(COINS[coin] * count for coin, count in coin_input.items())

def handle_payment(order_name, total_given):
    """Check if payment is sufficient and return success flag and change."""
    cost = MENU[order_name]["cost"]
    if total_given >= cost:
        change = round(total_given - cost, 2)
        return True, change
    return False, 0

def update_resources(order_name):
    """Deduct used resources from the available stock."""
    for item, amount in MENU[order_name]["ingredients"].items():
        resources[item] -= amount
    resources["money"] += MENU[order_name]["cost"]

def serve_coffee(order_name):
    """Main routine for processing a coffee order."""
    missing = check_resources(order_name, resources)
    if missing:
        print(f"Sorry, there's not enough {', '.join(missing)}.")
        return

    coins_inserted = get_user_coins()
    total = process_coins(coins_inserted)
    success, change = handle_payment(order_name, total)

    if success:
        update_resources(order_name)
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {order_name} ☕. Enjoy!\n")
    else:
        print("Sorry, that's not enough money. Money refunded.\n")

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Shutting down...")
            break
        elif choice == "report":
            report(resources)
        elif choice in MENU:
            serve_coffee(choice)
        else:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.\n")

# Run the program
coffee_machine()
