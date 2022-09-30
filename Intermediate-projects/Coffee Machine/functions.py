from machine_resources import MENU as mn


def coffee_choice(choose):
    if choose == 'espresso':
        water = mn['espresso']['ingredients']['water']
        coffee = mn['espresso']['ingredients']['coffee']
        cost = mn['espresso']['cost']
        return 'espresso'
    elif choose == 'late':
        return 'late'
    elif choose == 'cappuccino':
        return 'cappuccino'
    elif choose == 'report':

        return 'report'
    else:
        return "Only choose between 'espresso', 'late' or 'cappuccino'."


def coins_change(coin, units):
    if coin == "quarters":
        return units * 0.25
    elif coin == "dimes":
        return units * 0.10
    elif coin == "nickles":
        return units * 0.05
    else:
        return units * 0.01


def resources_left(water, coffee, cost, milk=0):
    return milk
