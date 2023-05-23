import os
from database.database_setup import create_database
from menu.functions import create_menu
from menu.menu_functions import perform_manage_action, perform_data_action, show_currency_menu, perform_currency_action
from menu.data_functions import show_data

def show_currency_menu():
    currency_menu_title = "Currency Menu"
    currency_menu_items = ["Simulate Currency", "View Currency History", "Back"]
    currency_menu = create_menu(currency_menu_title, currency_menu_items)
    currency_menu.show()
    return currency_menu.chosen_menu_index


def show_manage_menu():
    manage_menu_title = "Manage Menu"
    manage_menu_items = ["Manage Countries", "Manage Cities", "Manage Shops", "Manage Items", "Manage Item Types", "Back"]
    manage_menu = create_menu(manage_menu_title, manage_menu_items)
    manage_menu.show()
    return manage_menu.chosen_menu_index


def show_data_menu():
    data_menu_title = "Data Menu"
    data_menu_items = ["Import Shop", "Export Shop", "Back"]
    data_menu = create_menu(data_menu_title, data_menu_items)
    data_menu.show()
    return data_menu.chosen_menu_index


if __name__ == "__main__":
    if not os.path.exists("virtual_economy.sqlite"):
        print("Database not found. Creating a new database...")
        create_database()
    while True:
        main_menu_title = "Virtual Economy Menu"
        main_menu_items = ["Currency", "Manage", "Data", "Show Data", "Exit"]
        main_menu = create_menu(main_menu_title, main_menu_items)
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
                if manage_choice == 5:
                    break
                perform_manage_action(manage_choice)

        elif main_choice == 2:
            while True:
                data_choice = show_data_menu()
                if data_choice == 2:
                    break
                perform_data_action(data_choice)

        elif main_choice == 3:
            show_data()
        
        elif main_choice == 4:
            exit()
