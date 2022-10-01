from functions import coffee_choice, total_coins_change
from machine_resources import MENU, resources

resources["money"] = 0


while True:
    coffee_choose = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_choose != "report":
        print("Please insert coins.")

        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        total = total_coins_change(quarters, dimes, nickles, pennies, coffee_choose)

        print(total)

        if total != "Sorry, that's not enough money. Money refunded.":
            print(coffee_choice(coffee_choose))

            if coffee_choice(coffee_choose) == "Here is your ☕. Enjoy!":
                resources["water"] -= MENU[coffee_choose]["ingredients"]["water"]
                resources["milk"] -= MENU[coffee_choose]["ingredients"]["water"]
                resources["coffee"] -= MENU[coffee_choose]["ingredients"]["water"]
                resources["money"] += MENU[coffee_choose]["cost"]

    if coffee_choose == "report":
        print(coffee_choice(coffee_choose))
