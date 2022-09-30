from functions import coffee_choice

while True:
    coffee_choose = input("What would you like? (espresso/late/cappuccino): ")

    print(coffee_choice(coffee_choose))
