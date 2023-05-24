from currency import *
from manageOptions import *
from importExport import *
from showData import * 
from createDatabase import *
from library import *
from time import sleep

import os
import sqlite3
from simple_term_menu import TerminalMenu

def perform_currency_action(choice):
    if choice == 0:
        simulate()
    elif choice == 1:
        currency = VirtualCurrency()
        currency.plot_history()


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
    elif choice == 5:
        show_tables_menu()


def perform_data_action(choice):
    if choice == 0:
        import_item_list()
    elif choice == 1:
        export_item_list()


def show_currency_menu():
    currency_menu_title = "Currency Menu"
    currency_menu_items = ["Simulate Currency", "View Currency History", "Back"]
    currency_menu = basic_menu(currency_menu_title, currency_menu_items)
    currency_menu.show()
    return currency_menu.chosen_menu_index


def show_manage_menu():
    manage_menu_title = "Manage Menu"
    manage_menu_items = ["Manage Countries", "Manage Cities", "Manage Shops", "Manage Items", "Manage Item Types", "Show Data", "Back"]
    manage_menu = basic_menu(manage_menu_title, manage_menu_items)
    manage_menu.show()
    return manage_menu.chosen_menu_index


def show_data_menu():
    data_menu_title = "Data Menu"
    data_menu_items = ["Import Shop", "Export Shop", "Back"]
    data_menu = basic_menu(data_menu_title, data_menu_items)
    data_menu.show()
    return data_menu.chosen_menu_index


if __name__ == "__main__":
    if not os.path.exists(DATABASE_NAME):
        print(colored("Database not found. Creating a new database...", color='green', attrs=['bold']))
        create_database()
    while True:
        main_menu_title = "Virtual Economy Menu"
        main_menu_items = ["Currency", "Manage", "Data", "Exit"]
        main_menu = basic_menu(main_menu_title, main_menu_items)
        main_choice = main_menu.show()

        if main_choice == 0:
            while True:
                currency_choice = show_currency_menu()
                if currency_choice == 2:
                    break
                perform_currency_action(currency_choice)

        elif main_choice == 1:
            while True:
                manage_choice = show_manage_menu()
                if manage_choice == 6:
                    break
                perform_manage_action(manage_choice)

        elif main_choice == 2:
            while True:
                data_choice = show_data_menu()
                if data_choice == 2:
                    break
                perform_data_action(data_choice)

        elif main_choice == 3:
            exit()
