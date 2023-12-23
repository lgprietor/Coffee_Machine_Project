# TODO: 1 - Create and import a logo

from art import logo
from data import MENU, resources

print(logo)

# TODO 4: In order to report the current money in the machine is necessary to create a global variable money to save
#  there the coins and the money used

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

print(user_coffee_selected)


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

# TODO: 6 - Create a function to process the coins

check_resources(user_coffee_selected)

# if check_resources(user_coffee_selected) == True:
