from database.database_operation import *
from .functions import basic_menu, select_city_menu, select_country_menu, select_shop_menu
from termcolor import colored


def add_item_prompt():
    name = input(colored("Enter the name of the item: ", attrs=['bold']))
    current_price = float(input(colored("Enter the current price of the item: ", attrs=['bold'])))
    min_price = float(input(colored("Enter the minimum price of the item: ", attrs=['bold'])))
    max_price = float(input(colored("Enter the maximum price of the item: ", attrs=['bold'])))
    current_amount = int(input(colored("Enter the current amount of the item: ", attrs=['bold'])))

    country = select_country_menu()
    if not country:
        return

    city = select_city_menu(country.id)
    if not city:
        return

    shop = select_shop_menu(city.id)
    if not shop:
        return

    # Select the item type
    item_types = get_item_types()
    item_type_menu_items = [f"{item_type.type} - {item_type.sub_type}" for item_type in item_types]
    item_type_menu_items.append("Back")
    item_type_menu = basic_menu("Select an item type", item_type_menu_items)
    item_type_choice = item_type_menu.show()

    if item_type_choice == len(item_type_menu_items) - 1:
        return

    item_type_id = item_types[item_type_choice].id

    add_item(name, current_price, min_price, max_price, current_amount, item_type_id, shop.id)
    print(colored("Item added successfully.", "green"))


def remove_item_prompt():
    items = get_items()
    if not items:
        print(colored("No items available.", "yellow"))
        return

    item_menu_items = [f"{item.name}" for item in items]
    item_menu_items.append("Back")
    item_menu = basic_menu("Select an item to remove", item_menu_items)
    item_choice = item_menu.show()

    if item_choice == len(item_menu_items) - 1:
        return

    remove_item(items[item_choice].id)
    print(colored("Item removed successfully.", "green"))


def edit_item_prompt():
    items = get_items()
    if not items:
        print(colored("No items available.", "yellow"))
        return

    item_menu_items = [f"{item.name}" for item in items]
    item_menu_items.append("Back")
    item_menu = basic_menu("Select an item to edit", item_menu_items)
    item_choice = item_menu.show()

    if item_choice == len(item_menu_items) - 1:
        return

    new_name = input(colored("Enter the new name for the item: ", attrs=['bold']))
    new_current_price = float(input(colored("Enter the new current price for the item: ", attrs=['bold'])))
    new_min_price = float(input(colored("Enter the new minimum price for the item: ", attrs=['bold'])))
    new_max_price = float(input(colored("Enter the new maximum price for the item: ", attrs=['bold'])))
    new_current_amount = int(input(colored("Enter the new current amount for the item: ", attrs=['bold'])))

    country = select_country_menu()
    if not country:
        return

    city = select_city_menu(country.id)
    if not city:
        return

    shop = select_shop_menu(city.id)
    if not shop:
        return

    # Select the item type
    item_types = get_item_types()
    item_type_menu_items = [f"{item_type.type} - {item_type.sub_type}" for item_type in item_types]
    item_type_menu_items.append("Back")
    item_type_menu = basic_menu("Select an item type", item_type_menu_items)
    item_type_choice = item_type_menu.show()

    if item_type_choice == len(item_type_menu_items) - 1:
        return

    item_type_id = item_types[item_type_choice].id

    edit_item(items[item_choice].id, new_name, new_current_price, new_min_price, new_max_price,
              new_current_amount, item_type_id, shop.id)
    print(colored("Item edited successfully.", "green"))


def manage_items():
    while True:
        item_menu_title = "Manage Items"
        item_menu_items = ["Add Item", "Remove Item", "Edit Item", "Back"]
        item_menu = basic_menu(item_menu_title, item_menu_items)
        item_choice = item_menu.show()

        if item_choice == 0:
            add_item_prompt()

        elif item_choice == 1:
            remove_item_prompt()

        elif item_choice == 2:
            edit_item_prompt()

        elif item_choice == 3:
            break