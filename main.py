# TODO: 1 - Create and import a logo

from art import logo
from data import MENU, resources

print(logo)

# TODO 4: In order to report the current money in the machine is necessary to create a global variable money to save
#  there the coins and the money used - this should be joined with the dictionary of quantities of coins

money = []

# TODO 15.1: It's necessary to allow dictionary to be a global variable in order to gain access everywhere:

values_paid_dictionary = {
            "quarter": [],
            "dime": [],
            "nickel": [],
            "penny": [],
            "Money": [],
            "Change": [],
            "Total_money": [],
            "Refunds": [],
}

# TODO: 7 - It's necessary to create a dictionary to display on screen for user the coins options (Global)

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}

# TODO: 3 - Creating a report function that print on screen the balance of ingredients and money. This function was
#  written to allow user call the function in the ask_user_selection function

def report():
    print("The machine right now has the following resources: \n")
    for i in resources:
        if i == "water" or i == "milk":
            print(f"{i.title()}: {resources[i]} mL")
        else:
            print(f"{i.title()}: {resources[i]} g")

    for i in values_paid_dictionary:
        if i == "quarter" or i == "dime" or i == "nickel" or i == "penny":
            #print(f"{i} coins quantity {sum(values_paid_dictionary[i])}")
            money_calculated = (coins[i])*sum(values_paid_dictionary[i])
            values_paid_dictionary["Total_money"].append(money_calculated)

    #Print total

    Final_total = 0

    for j in range(-4, 0):
        Final_total += values_paid_dictionary["Total_money"][j]
        print(Final_total)

    Final_total -= sum(values_paid_dictionary["Change"]) - sum(values_paid_dictionary["Refunds"])
    # Final_change = sum(values_paid_dictionary["Change"])

    # print(values_paid_dictionary)

    #print(f"The change returned to user is: {Final_change}")
    print(f"Money: $USD {Final_total}")
    # print(values_paid_dictionary)


# TODO: 2 - Create a function that validates an input for coffee machine type. According to the
#  analysis, this validation must be done using a combination of while + if + else because is a string type
#  The user here has the option of select a type of coffee or he can select off function or report function:

def ask_usr_selection():
    usr_selection_validated = False

    while not usr_selection_validated:

        user_selection = input("What would you like? (espresso/latte/cappuccino) \n").lower()

        if user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":

            usr_selection_validated = True
            return user_selection

        elif user_selection == "off":
            print("Bye")
            return user_selection

        elif user_selection == "report":
            return user_selection

        else:
            print("Please write a valid option")


user_coffee_selected = ask_usr_selection()


# print(user_coffee_selected)


# TODO: 5 - Create a function that check resources sufficiency?

def check_resources(user_coffee_selected):
    # Check if there's enough resources to produce a coffee
    enough_resources = []
    missing_resources = []
    quantity_missing = []

    for ingredient in MENU[user_coffee_selected]["ingredients"]:
        if resources[ingredient] >= MENU[user_coffee_selected]["ingredients"][ingredient]:
            enough_resources.append(ingredient)
        else:
            ingredients_difference = abs(resources[ingredient] - MENU[user_coffee_selected]["ingredients"][ingredient])
            missing_resources.append(ingredient)
            quantity_missing.append(ingredients_difference)

    if len(missing_resources) == 0:
        resources_checked = True
    else:
        print("Sorry, there is not enough ingredients to prepare the coffee selected")
        resources_checked = False
        for i in range(0, len(missing_resources)):
            if i == "water" or "milk":
                measuring_unit = "mL"
            else:
                measuring_unit = "g"

            print(f"Please refill the machine with {quantity_missing[i]} {measuring_unit} of {missing_resources[i]}")

    return resources_checked


# TODO: 6 - Create a function to process the coins. This function has more functions inside

def check_coins_function(resources_status):
    if resources_status:

        print("This machine receives this type of coins: \n")

        for i in coins:
            print(f"{i.title()} coin $USD {coins[i]}")

        # TODO: 8 - Create a function that validates an input for coin type

        def coin_selection_validated(user_coffee_selected):

            coin_selection_checked = False

            while not coin_selection_checked:

                coin_selection = input(f"\n What coin do you want to use to pay your {user_coffee_selected}? Please "
                                       f"select A for quarters,B for dimes, C for nickels, and D for pennies \n")

                if coin_selection == "A" or coin_selection == "B" or coin_selection == "C" or coin_selection == "D":
                    coin_selection_checked = True
                else:
                    print("Please write a valid option")

            return coin_selection

        coin_selected = coin_selection_validated(user_coffee_selected)

        # TODO: 9 - Create a function that translate the user option in coin selection validated:

        def coins_type_translation(coin_selected):

            if coin_selected == "A":
                coin_translated = "quarter"
                return coin_translated
            elif coin_selected == "B":
                coin_translated = "dime"
                return coin_translated
            elif coin_selected == "C":
                coin_translated = "nickel"
                return coin_translated
            elif coin_selected == "D":
                coin_translated = "penny"
                return coin_translated

        # TODO: 10 - Create a function that validates the amount of coins received from user:

        coin_selected_translated = coins_type_translation(coin_selected)

        def coins_used(coin_selected_translated):

            # TODO: 11 - It's necessary to check the input from user. Due to the number of coins is an integer
            #  variable, it's useful to validate the input using a combination of while + try + except + else:'

            payment_checked = False

            while not payment_checked:
                try:
                    if coin_selected_translated == "penny":
                        coin_selected_translated = "pennie"
                    number_of_coins = int(input(f"please insert the number of {coin_selected_translated}s: \n"))
                except:
                    print("Please write a number")
                else:
                    payment_checked = True

            return number_of_coins

        coins_paid = coins_used(coin_selected_translated)

        # TODO: 12 - Create a function to calculate the current paid value:

        def current_paid_value(coin_selected_translated, coins_paid):

            calculated_paid_value = coins[coin_selected_translated] * coins_paid

            return calculated_paid_value

        calculated_payment = (current_paid_value(coin_selected_translated, coins_paid))

        # TODO: 15 - It's necessary to create a function that saves the quantities of type of coin, and quantity
        #  calculated to facilitate the calculation in each payment iteration:

        def value_saver(coin_selected_translated, coins_paid, calculated_payment):

            values_paid_dictionary[coin_selected_translated].append(coins_paid)

            values_paid_dictionary["Money"].append(calculated_payment)

        value_saver(coin_selected_translated, coins_paid, calculated_payment)

        # TODO: 14 - It's necessary to create a function that ask user if he wants to continue paying

        def continue_payment():

            continue_payment_checked = False

            while not continue_payment_checked:

                user_continue_payment = input("Do you want to continue with the payment? "
                                              "Type yes or no \n").lower()

                if user_continue_payment == "yes" or user_continue_payment == "y":

                    continue_payment_checked = True

                elif user_continue_payment == "no" or user_continue_payment == "n":

                    continue_payment_checked = True

                else:

                    print("Please write a valid option")

            return user_continue_payment

        # TODO: 13 - Create a function that checks the payment completion

        def payment_completion(user_coffee_selected, calculated_payment):

            difference = (MENU[user_coffee_selected]["cost"] - calculated_payment)

            payment_checked = False

            while not payment_checked:

                if difference < 0:

                    change = abs(difference)

                    print(f"It was a pleasure to serve you, there you go, you have your "
                          f"{user_coffee_selected} 🍵🍵🍵🍵 and your $USD {change} change")

                    values_paid_dictionary["Change"].append(change)
                    payment_checked = True
                    transaction_checked = True

                elif difference == 0:

                    print(f"It was a pleasure to serve you, here you go, you have your "
                          f"{user_coffee_selected} 🍵🍵🍵🍵")

                    payment_checked = True
                    transaction_checked = True

                while difference > 0:

                    print(f"You current paid is $ USD {calculated_payment}. Please insert $ USD {difference} to "
                          f"get you {user_coffee_selected}")

                    user_continue_payment = continue_payment()

                    if user_continue_payment == "no":

                        print(f"Your funds $USD {calculated_payment} have been refunded")
                        values_paid_dictionary["Refunds"].append(calculated_payment)
                        return

                    elif user_continue_payment == "yes":

                        coin_selected = coin_selection_validated(user_coffee_selected)
                        coin_selected_translated = coins_type_translation(coin_selected)
                        coins_paid = coins_used(coin_selected_translated)
                        calculated_payment = (current_paid_value(coin_selected_translated, coins_paid))

                        calculated_payment2 = (calculated_payment + values_paid_dictionary["Money"][-1])

                        value_saver(coin_selected_translated, coins_paid, calculated_payment2)

                        difference2 = (MENU[user_coffee_selected]["cost"] - calculated_payment2)

                        calculated_payment = calculated_payment2

                        difference = difference2

            return transaction_checked

        status_transaction = (payment_completion(user_coffee_selected, calculated_payment))

        # TODO: 16 - Create a function that subtracts the quantities of resources used to produce a cup of coffee
        def quantities_subtraction(status_transaction, user_coffee_selected):

            if status_transaction:

                for i in MENU[user_coffee_selected]["ingredients"]:
                    resources[i] = resources[i] - MENU[user_coffee_selected]["ingredients"][i]

            else:
                return

            # print(resources)

        quantities_subtraction(status_transaction, user_coffee_selected)

        # print(values_paid_dictionary)

        return status_transaction

    else:
        return

# TODO: 17 - It's necessary to call the function to get a coffee by the first time

if user_coffee_selected == "espresso" or user_coffee_selected == "latte" or user_coffee_selected == "cappuccino":
    coffee_cost = MENU[user_coffee_selected]["cost"]

    print(f"The {user_coffee_selected} costs $USD {coffee_cost}")

    resources_status = check_resources(user_coffee_selected)

    new_coffee = check_coins_function(resources_status)

elif user_coffee_selected == "report":
    report()
    new_coffee = True

elif user_coffee_selected == "off":
    new_coffee = False

# TODO: 18 - Create a recursion function to ask user for another coffee:
def recursion_coffee():

    print(logo)

    global user_coffee_selected

    user_coffee_selected = ask_usr_selection()

    if user_coffee_selected == "espresso" or user_coffee_selected == "latte" or user_coffee_selected == "cappuccino":

        coffee_cost = MENU[user_coffee_selected]["cost"]

        print(f"The {user_coffee_selected} costs $USD {coffee_cost}")

        resources_status = check_resources(user_coffee_selected)

        new_coffee = check_coins_function(resources_status)

        return new_coffee

    elif user_coffee_selected == "report":

        report()

        new_coffee = True

        return new_coffee


    elif user_coffee_selected == "off":

        new_coffee = False

        return new_coffee

while new_coffee:
    new_coffee = recursion_coffee()






