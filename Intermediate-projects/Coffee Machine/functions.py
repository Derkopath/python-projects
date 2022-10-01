from machine_resources import MENU, resources


def coffee_choice(choose):
    if choose == 'espresso':
        water = MENU['espresso']['ingredients']['water']
        coffee = MENU['espresso']['ingredients']['coffee']
        """cost = MENU['espresso']['cost']"""
        return coffee_maker(water, coffee)
    elif choose == 'late':
        return 'late'
    elif choose == 'cappuccino':
        return 'cappuccino'
    elif choose == 'report':
        return f"Water: {resources['water']}ml \n" \
               f"Milk: {resources['milk']}ml \n" \
               f"Coffee: {resources['water']}ml \n" \
               f"Money: $0"
    else:
        return "Only choose between 'espresso', 'late' or 'cappuccino'."


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


def coins_change(coin, units):
    if coin == "quarters":
        return units * 0.25
    elif coin == "dimes":
        return units * 0.10
    elif coin == "nickles":
        return units * 0.05
    else:
        return units * 0.01


def total_coins_change(quarters, dimes, nickles, pennies):

    total = quarters + dimes + nickles + pennies

    return total

