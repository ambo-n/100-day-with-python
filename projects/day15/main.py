MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def report(resource_data):
    """Return the current resources of the coffee machine"""
    print(f"\nResource Report:")
    print(f"Water: {resource_data.get('water',0)} mL")
    print(f"Milk: {resource_data.get('milk',0)} mL")
    print(f"Coffee: {resource_data.get('coffee',0)} g")
    print(f"Money: ${resource_data.get('money',0):.2f}\n")

def check_resources(order, resource_data):
    """Check if resources are sufficient for the order"""
    ingredients = MENU[order]["ingredients"]
    ingredients_needed = []
    for item in ingredients:
        if ingredients[item] > resource_data.get(item,0):
            ingredients_needed.append(item)
    return ingredients_needed

def process_coins(user_money):
    total =0
    for key, value in user_money.items():
        total += coins[key]*value
    return total

def check_money(order,total_amount_given):
    cost = MENU[order]["cost"]
    if total_amount_given >= cost:
        global resources
        resources["money"] += cost
        change = round(total_amount_given-cost,2)
        return True, change
    else:
        return False,0

def resource_control(order):
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

def coffee_machine(request):
    if request == 'report':
        report(resources)
    else:
        not_enough_of = check_resources(request, resources)
        if not_enough_of:
            print(f"Sorry there is not enough of {", ".join(not_enough_of)}")
            return
        else:
            print("Please insert coins")
            user_money = {}
            user_money["quarters"] = int(input("How many quarters?: "))
            user_money["dimes"] = int(input("How many dimes?: "))
            user_money["nickels"] = int(input("How many nickles?: "))
            user_money["pennies"] = int(input("How many pennies?: "))
            money_given = process_coins(user_money)
            success, change = check_money(request, money_given)
            if success:
                print(f"Here's your {request} ☕ Enjoy!")
                if change >0:
                    print(f"Here's ${change} in change")
                resource_control(request)
            else:
                print("Sorry that's not enough money. Money refunded")
                
def main():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == 'off':
            break
        coffee_machine(user_input)

main()