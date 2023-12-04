from resc_menu import MENU, resources

# Initializing constants
QUARTER = 0.25
NICKEL = 0.10
DIME = 0.05
PENNY = 0.01


def resources_avl(resources):
    for key in resources:
        if key == "money" and resources["money"] == 0:
            continue
        print(f"{key}: {resources[key]}")


def check_resources(user_choice, resources):
    if user_choice == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return True

    elif user_choice == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            return True

    elif user_choice == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            return True

    return False


# 5. Process coins.
def process_coins(cost):
    print("Please insert the coins.")
    q_coins = int(input("How many quarters?: "))
    n_coins = int(input("How many nickels?: "))
    d_coins = int(input("How many dimes?: "))
    p_coins = int(input("How many pennies?: "))
    coins = [QUARTER * q_coins, NICKEL * n_coins, DIME * d_coins, PENNY * p_coins]
    total = sum(coins)
    # print(total)
    change = total - cost
    if change >= 0:
        return change

    else:
        return False


def coffee(change, user_choice, money):
    if user_choice == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
        money += 1.5

    elif user_choice == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        money += 2.5

    elif user_choice == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        money += 3.0

    if change == 0:
        print("There is no change left.")

    else:
        print(f"Here is the change ${change}.")

    print(f"Here is your {user_choice}. Enjoy")
    resources["money"] += money
    print(resources["money"])

cost = 0
money = 0
while True:
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # a. Check the user’s input to decide what to do next.
    if user_choice == "latte" or user_choice == "espresso" or user_choice == "cappuccino":
        cost = MENU[user_choice]["cost"]
    # Done
    # 3. Print report.
    if user_choice == "report":
        resources_avl(resources)

    # Done
    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif user_choice == "off":
        exit()

    else:
        # 4. Check resources sufficient?
        if check_resources(user_choice, resources):
            change = process_coins(cost)
            # 6. Check transaction successful?
            if not change:
                print("Sorry that is not enough money. Money is refunded")
            # 7. Make Coffee.
            else:
                coffee(change, user_choice, money)

        else:
            print("Sorry there are not enough resources to make your coffee. Check and refill the supplies.")


