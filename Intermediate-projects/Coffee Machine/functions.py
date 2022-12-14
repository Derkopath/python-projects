from machine_resources import MENU, resources

"""
Condition:
    - If the user writes another option, this function returns an "error" message.
    - Else if the user writes ('espresso', 'latte' or 'capuccino') the machine returns the coffee if everything is ok.
    - Or the machine will return how many resources left (with 'report' option).
"""


def coffee_choice(choose):
    if choose == 'espresso':

        water = MENU[choose]['ingredients']['water']
        coffee = MENU[choose]['ingredients']['coffee']

        return coffee_maker(water, coffee)
    elif choose == 'latte':
        water = MENU[choose]['ingredients']['water']
        coffee = MENU[choose]['ingredients']['coffee']
        milk = MENU[choose]['ingredients']['milk']

        return coffee_maker(water, coffee, milk)
    elif choose == 'cappuccino':
        water = MENU[choose]['ingredients']['water']
        coffee = MENU[choose]['ingredients']['coffee']
        milk = MENU[choose]['ingredients']['milk']

        return coffee_maker(water, coffee, milk)
    elif choose == 'report':
        return f"Water: {resources['water']}ml \n" \
               f"Milk: {resources['milk']}ml \n" \
               f"Coffee: {resources['water']}g \n" \
               f"Money: ${resources['money']}"
    else:
        return "Only choose between 'espresso', 'latte' or 'cappuccino'."


"""
Condition:
    - If 'resources' has enough ingredients this function will return the coffee made.
    - Else if one of those ingredients is not enough, return the reason why the machine cannot make coffee.
"""


def coffee_maker(water, coffee, milk=0):
    machine_water = resources["water"]
    machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]

    if machine_water >= water and machine_milk >= milk and machine_coffee >= coffee:
        return "Here is your ☕. Enjoy!"
    elif water > machine_water:
        return "Sorry, there's not enough water. Money refunded."
    elif milk > 0 and milk > machine_milk:
        return "Sorry, there's not enough milk. Money refunded."
    elif coffee > machine_coffee:
        return "Sorry, there's not enough coffee. Money refunded."
    else:
        return "Sorry, something's wrong. Money refunded."


# Make a change of the coin multiply 'units' with the real value of that coin.

def coins_change(coin, units):
    if coin == "quarters":
        return units * 0.25
    elif coin == "dimes":
        return units * 0.10
    elif coin == "nickles":
        return units * 0.05
    else:
        return units * 0.01


"""
args:
    - 'coins': saves the type of coin and the value.
    - 'total': returns the addition of the values inside the dictionary.

Condition:
    - If 'total' is smaller than the price of the coffee (coffee_price), this function returns an "error" message.
"""


def total_coins_change(quarters, dimes, nickles, pennies, coffee_choose):
    coins = {"quarters": quarters, "dimes": dimes, "nickles": nickles, "pennies": pennies}
    total = 0
    coffee_price = MENU[coffee_choose]['cost']

    for coin in coins:
        total += coins_change(coin, coins[coin])

    if coffee_price > total:
        return "Sorry, that's not enough money. Money refunded."

    return f"Here is ${total} in change."
