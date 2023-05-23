from database.database_operation import *
from .functions import create_menu
from termcolor import colored


def add_country_prompt():
    name = input(colored("Enter the name of the country: ", attrs=['bold']))
    add_country(name)
    print(colored("Country added successfully.", "green"))


def remove_country_prompt():
    countries = get_countries()
    if not countries:
        print(colored("No countries available.", "yellow"))
        return

    country_menu_items = [f"{country.name}" for country in countries]
    country_menu_items.append("Back")
    country_menu = create_menu("Select a country to remove", country_menu_items)
    country_choice = country_menu.show()

    if country_choice == len(country_menu_items) - 1:
        return

    remove_country(countries[country_choice].id)
    print(colored("Country removed successfully.", "green"))


def edit_country_prompt():
    countries = get_countries()
    if not countries:
        print(colored("No countries available.", "yellow"))
        return

    country_menu_items = [f"{country.name}" for country in countries]
    country_menu_items.append("Back")
    country_menu = create_menu("Select a country to edit", country_menu_items)
    country_choice = country_menu.show()

    if country_choice == len(country_menu_items) - 1:
        return

    new_name = input(colored("Enter the new name for the country: ", attrs=['bold']))
    edit_country(countries[country_choice].id, new_name)
    print(colored("Country edited successfully.", "green"))


def manage_countries():
    while True:
        country_menu_title = "Manage Countries"
        country_menu_items = ["Add Country", "Remove Country", "Edit Country", "Back"]
        country_menu = create_menu(country_menu_title, country_menu_items)
        country_choice = country_menu.show()

        if country_choice == 0:
            add_country_prompt()

        elif country_choice == 1:
            remove_country_prompt()

        elif country_choice == 2:
            edit_country_prompt()

        elif country_choice == 3:
            break