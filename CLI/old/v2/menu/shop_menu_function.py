from database.database_operation import *
from .functions import basic_menu, select_country_menu, select_city_menu
from termcolor import colored


def add_shop_prompt():
    name = input(colored("Enter the name of the shop: ", attrs=['bold']))

    country = select_country_menu()
    if not country:
        return

    city = select_city_menu(country.id)
    if not city:
        return

    add_shop(name, city.id)
    print(colored("Shop added successfully.", "green"))


def remove_shop_prompt():
    shops = get_shops()
    if not shops:
        print(colored("No shops available.", "yellow"))
        return

    shop_menu_items = [f"{shop.name}" for shop in shops]
    shop_menu_items.append("Back")
    shop_menu = basic_menu("Select a shop to remove", shop_menu_items)
    shop_choice = shop_menu.show()

    if shop_choice == len(shop_menu_items) - 1:
        return

    remove_shop(shops[shop_choice].id)
    print(colored("Shop removed successfully.", "green"))


def edit_shop_prompt():
    shops = get_shops()
    if not shops:
        print(colored("No shops available.", "yellow"))
        return

    shop_menu_items = [f"{shop.name}" for shop in shops]
    shop_menu_items.append("Back")
    shop_menu = basic_menu("Select a shop to edit", shop_menu_items)
    shop_choice = shop_menu.show()

    if shop_choice == len(shop_menu_items) - 1:
        return

    new_name = input(colored("Enter the new name for the shop: ", attrs=['bold']))

    country = select_country_menu()
    if not country:
        return

    city = select_city_menu(country.id)
    if not city:
        return

    edit_shop(shops[shop_choice].id, new_name, city.id)
    print(colored("Shop edited successfully.", "green"))


def manage_shops():
    while True:
        shop_menu_title = "Manage Shops"
        shop_menu_items = ["Add Shop", "Remove Shop", "Edit Shop", "Back"]
        shop_menu = basic_menu(shop_menu_title, shop_menu_items)
        shop_choice = shop_menu.show()

        if shop_choice == 0:
            add_shop_prompt()

        elif shop_choice == 1:
            remove_shop_prompt()

        elif shop_choice == 2:
            edit_shop_prompt()

        elif shop_choice == 3:
            break