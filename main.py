# TODO: 1 - Create and import a logo

from art import logo

print(logo)


# TODO: 2 - Create a function that validates an input for coffee machine type. According to the analysis:

def ask_usr_selection():
    usr_selection_validated = False

    while not usr_selection_validated:

        user_selection = input("What would you like? (espresso/latte/cappuccino").lower()

        if user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":

            usr_selection_validated = True
            return user_selection

        else:
            "Please write a valid option"


ask_usr_selection()
