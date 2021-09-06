inventory = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
    "money": 0,
}

menu = {
    "1": {
        "water": 200,
        "milk": 50,
        "coffee": 50,
        "money": 1.50,
    },
    "2": {
        "water": 200,
        "milk": 100,
        "coffee": 50,
        "money": 2.50,
    },
    "3": {
        "water": 100,
        "milk": 20,
        "coffee": 20,
        "money": 0.50,
    },
}


def greeting():
    user_input = input("\nHello! Would you like some coffee?\n"
                       "Press:\n"
                       "1 for Cappuccino\n"
                       "2 for Latte Macchiato\n"
                       "3 for Espresso\n\n"
                       "Your choice: ")

    return user_input


def report():
    water = inventory["water"]
    milk = inventory["milk"]
    coffee = inventory["coffee"]
    money = inventory["money"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}ml")
    print(f"Money: {money}$")


def check_resource(user_choice):
    water_inventory = inventory["water"]
    milk_inventory = inventory["milk"]
    coffee_inventory = inventory["coffee"]

    water_cost = menu[user_choice]["water"]
    milk_cost = menu[user_choice]["milk"]
    coffee_cost = menu[user_choice]["coffee"]

    if water_inventory >= water_cost and milk_inventory >= milk_cost and coffee_inventory >= coffee_cost:
        return True
    else:
        print("Not enough resources. Call XXX")
        return False


def process_payment(user_choice):
    item_cost = menu[user_choice]["money"]
    user_funds = 0

    while True:
        print(f"Your drink costs: {item_cost}$.\n"
              f"Your funds are: {round(user_funds, 2)}$")
        try:
            money_input = float(input("\nInsert Money (Write number)\n"))
        except ValueError:
            print("INPUT ERROR\n"
                  "Only numbers allowed!\n")
            continue
        else:
            user_funds += money_input

        if user_funds == item_cost:
            inventory["money"] += item_cost
            print("Transaction successful!")
            break
        elif user_funds > item_cost:
            change = user_funds - item_cost
            inventory["money"] += item_cost
            print(f"Transaction successful! Your change amounts to {round(change, 2)}$")
            break
        else:
            print("Insufficient funds!")


def make_coffee(user_choice):
    water_cost = menu[user_choice]["water"]
    milk_cost = menu[user_choice]["milk"]
    coffee_cost = menu[user_choice]["coffee"]

    inventory["water"] -= water_cost
    inventory["milk"] -= milk_cost
    inventory["coffee"] -= coffee_cost

    print("Your coffee is ready. Enjoy!")


def refill():
    inventory["water"] = 1000
    inventory["milk"] = 1000
    inventory["coffee"] = 1000
