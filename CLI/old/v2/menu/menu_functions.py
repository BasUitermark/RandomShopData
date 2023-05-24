from database.database_operation import *
from .country_menu_functions import manage_countries
from .city_menu_functions import manage_cities
from .shop_menu_function import manage_shops
from .item_menu_functions import manage_items
from .item_type_menu_funtions import manage_item_types
from .import_functions import import_item_list
from .data_functions import show_data

def perform_currency_action(choice):
    return
    # if choice == 0:
    #     simulate()
    # elif choice == 1:
    #     currency = VirtualCurrency()
    #     currency.plot_history()

def perform_manage_action(choice):
    if choice == 0:
        manage_countries()
    elif choice == 1:
        manage_cities()
    elif choice == 2:
        manage_shops()
    elif choice == 3:
        manage_items()
    elif choice == 4:
        manage_item_types()


def perform_data_action(choice):
    if choice == 0:
        import_item_list()
    # elif choice == 1:
    #     export_item_list()


def show_currency_menu():
    currency_menu_title = "Currency Menu"
    currency_menu_items = ["Simulate Currency", "View Currency History", "Back"]
    currency_menu = basic_menu(currency_menu_title, currency_menu_items)
    currency_menu.show()
    return currency_menu.chosen_menu_index