# TODO: 1 - Create and import a logo

from art import logo
from data import MENU, resources

print(logo)

# TODO 4: In order to report the current money in the machine is necessary to create a global variable money to save
#  there the coins and the money used - this should be joined with the dictionary of quantities of coins

money = []


# TODO: 3 - Creating a report function that print on screen the balance of ingredients and money. This function was
#  written to allow user call the function in the ask_user_selection function

def report():
    print("The machine right now has the following resources: \n")
    for i in resources:
        if i == "water" or i == "milk":
            print(f"{i.title()} = {resources[i]} mL")
        else:
            print(f"{i.title()} = {resources[i]} g")
    print(f"Money: ${sum(money)}")


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
            return

        elif user_selection == "report":
            report()
            return

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

resources_status = check_resources(user_coffee_selected)


def check_coins_function():
    if resources_status:

        # TODO: 7 - It's necessary to create a dictionary to display on screen for user the coins options

        coins = {
            "quarter": 0.25,
            "dime": 0.10,
            "nickel": 0.05,
            "penny": 0.01,
        }

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

        values_paid_dictionary = {
        "quarter": [],
        "dime": [],
        "nickel": [],
        "penny": [],
        "Total_paid": []
        }

        def value_saver(coin_selected_translated, coins_paid, calculated_payment):

            values_paid_dictionary[coin_selected_translated].append(coins_paid)

            values_paid_dictionary["Total_paid"].append(calculated_payment)

        value_saver(coin_selected_translated, coins_paid, calculated_payment)

        # TODO: 13 - Create a function that checks the payment completion

        def payment_completion(user_coffee_selected, calculated_payment):

            difference = (MENU[user_coffee_selected]["cost"] - calculated_payment)

            payment_checked = False

            while not payment_checked:

                if difference > 0:

                    print(f"You current paid is $ USD {calculated_payment}. Please insert $ USD {difference} to "
                          f"get you {user_coffee_selected}")

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

                    if continue_payment() == "yes":

                        coin_selected = coin_selection_validated(user_coffee_selected)
                        coin_selected_translated = coins_type_translation(coin_selected)
                        coins_paid = coins_used(coin_selected_translated)
                        calculated_payment = (current_paid_value(coin_selected_translated, coins_paid))

                        calculated_payment2 = calculated_payment + sum(values_paid_dictionary["Total_paid"])

                        value_saver(coin_selected_translated, coins_paid, calculated_payment2)

                        difference2 = (MENU[user_coffee_selected]["cost"] - calculated_payment2)

                        calculated_payment = calculated_payment2

                        if difference2 == 0:
                            print(f"It was a pleasure to serve you, there you go, you have your "
                                  f"{user_coffee_selected}")

                        if difference2 < 0:

                            change = difference2

                            print(f"It was a pleasure to serve you, there you go, you have your "
                                  f"{}user_coffee_selected} and your {change}")

                    if continue_payment() == "no":

                        return









        payment_completion(user_coffee_selected, calculated_payment)



















    else:
        return


check_coins_function()
