from functions import coffee_choice, total_coins_change
from machine_resources import MENU, resources

# Creates an instance into 'resources' dictionary.
resources["money"] = 0


while True:
    coffee_choose = input("What would you like? (espresso/latte/cappuccino): ")

    # If you select one of the three options, the machine ask you how many coins are you going to use.
    if coffee_choose != "report":
        print("Please insert coins.")

        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        total = total_coins_change(quarters, dimes, nickles, pennies, coffee_choose)

        print(total)

        """
        Condition:
            - If 'total' returns 'your coins are enough', the machine will proceed to make that coffee.     
        """

        if total != "Sorry, that's not enough money. Money refunded.":
            print(coffee_choice(coffee_choose))

            # This will remove resources used to make the coffee and add the money earned.
            if coffee_choice(coffee_choose) == "Here is your ☕. Enjoy!":
                resources["water"] -= MENU[coffee_choose]["ingredients"]["water"]
                resources["milk"] -= MENU[coffee_choose]["ingredients"]["water"]
                resources["coffee"] -= MENU[coffee_choose]["ingredients"]["water"]
                resources["money"] += MENU[coffee_choose]["cost"]

    # Returns how many resources left.
    if coffee_choose == "report":
        print(coffee_choice(coffee_choose))
