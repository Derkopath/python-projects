from functions import coffee_choice, total_coins_change, coins_change
from machine_resources import MENU, resources

while True:
    """coffee_choose = input("What would you like? (espresso/late/cappuccino): ")
    """

    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    print(total_coins_change(coins_change("quarters", quarters), coins_change("dimes", dimes), coins_change("nickles", nickles), coins_change("pennies", pennies)))

"""
    print(coffee_choice(coffee_choose))

    if coffee_choice(coffee_choose) == "☕":
        resources["water"] -= MENU[coffee_choose]["ingredients"]["water"]
"""
