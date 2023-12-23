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

# TODO

