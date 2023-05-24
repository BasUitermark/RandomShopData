from database.database_operation import *
from .functions import basic_menu, select_country_menu
from termcolor import colored


def add_city_prompt():
    name = input(colored("Enter the name of the city: ", attrs=['bold']))
    population = int(input(colored("Enter the population of the city: ", attrs=['bold'])))
    wealth_indicator = float(input(colored("Enter the wealth indicator of the city: ", attrs=['bold'])))

    country = select_country_menu()
    if not country:
        return

    add_city(name, population, wealth_indicator, country.id)
    print(colored("City added successfully.", "green"))


def remove_city_prompt():
    cities = get_cities()
    if not cities:
        print(colored("No cities available.", "yellow"))
        return

    city_menu_items = [f"{city.name}" for city in cities]
    city_menu_items.append("Back")
    city_menu = basic_menu("Select a city to remove", city_menu_items)
    city_choice = city_menu.show()

    if city_choice == len(city_menu_items) - 1:
        return

    remove_city(cities[city_choice].id)
    print(colored("City removed successfully.", "green"))


def edit_city_prompt():
    cities = get_cities()
    if not cities:
        print(colored("No cities available.", "yellow"))
        return

    city_menu_items = [f"{city.name}" for city in cities]
    city_menu_items.append("Back")
    city_menu = basic_menu("Select a city to edit", city_menu_items)
    city_choice = city_menu.show()

    if city_choice == len(city_menu_items) - 1:
        return

    new_name = input(colored("Enter the new name for the city: ", attrs=['bold']))
    new_population = int(input(colored("Enter the new population for the city: ", attrs=['bold'])))
    new_wealth_indicator = float(input(colored("Enter the new wealth indicator for the city: ", attrs=['bold'])))

    country = select_country_menu()
    if not country:
        return

    edit_city(cities[city_choice].id, new_name, new_population, new_wealth_indicator, country.id)
    print(colored("City edited successfully.", "green"))


def manage_cities():
    while True:
        city_menu_title = "Manage Cities"
        city_menu_items = ["Add City", "Remove City", "Edit City", "Back"]
        city_menu = basic_menu(city_menu_title, city_menu_items)
        city_choice = city_menu.show()

        if city_choice == 0:
            add_city_prompt()

        elif city_choice == 1:
            remove_city_prompt()

        elif city_choice == 2:
            edit_city_prompt()

        elif city_choice == 3:
            break
