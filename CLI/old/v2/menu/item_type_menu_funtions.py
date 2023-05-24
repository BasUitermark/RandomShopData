from database.database_operation import *
from .functions import basic_menu
from termcolor import colored


def add_item_type_prompt():
    type = input(colored("Enter the type of the item: ", attrs=['bold']))
    sub_type = input(colored("Enter the sub-type of the item: ", attrs=['bold']))
    min_amount = int(input(colored("Enter the minimum amount of the item type: ", attrs=['bold'])))
    max_amount = int(input(colored("Enter the maximum amount of the item type: ", attrs=['bold'])))
    wealth_indicator = float(input(colored("Enter the wealth indicator of the item type: ", attrs=['bold'])))

    add_item_type(type, sub_type, min_amount, max_amount, wealth_indicator)
    print(colored("Item type added successfully.", "green"))


def remove_item_type_prompt():
    item_types = get_item_types()
    if not item_types:
        print(colored("No item types available.", "yellow"))
        return

    item_type_menu_items = [f"{item_type.type} - {item_type.sub_type}" for item_type in item_types]
    item_type_menu_items.append("Back")
    item_type_menu = basic_menu("Select an item type to remove", item_type_menu_items)
    item_type_choice = item_type_menu.show()

    if item_type_choice == len(item_type_menu_items) - 1:
        return

    remove_item_type(item_types[item_type_choice].id)
    print(colored("Item type removed successfully.", "green"))


def edit_item_type_prompt():
    item_types = get_item_types()
    if not item_types:
        print(colored("No item types available.", "yellow"))
        return

    item_type_menu_items = [f"{item_type.type} - {item_type.sub_type}" for item_type in item_types]
    item_type_menu_items.append("Back")
    item_type_menu = basic_menu("Select an item type to edit", item_type_menu_items)
    item_type_choice = item_type_menu.show()

    if item_type_choice == len(item_type_menu_items) - 1:
        return

    new_type = input(colored("Enter the new type for the item type: ", attrs=['bold']))
    new_sub_type = input(colored("Enter the new sub-type for the item type: ", attrs=['bold']))
    new_min_amount = int(input(colored("Enter the new minimum amount for the item type: ", attrs=['bold'])))
    new_max_amount = int(input(colored("Enter the new maximum amount for the item type: ", attrs=['bold'])))
    new_wealth_indicator = float(input(colored("Enter the new wealth indicator for the item type: ", attrs=['bold'])))

    edit_item_type(item_types[item_type_choice].id, new_type, new_sub_type, new_min_amount, new_max_amount,
                   new_wealth_indicator)
    print(colored("Item type edited successfully.", "green"))


def manage_item_types():
    while True:
        item_type_menu_title = "Manage Item Types"
        item_type_menu_items = ["Add Item Type", "Remove Item Type", "Edit Item Type", "Back"]
        item_type_menu = basic_menu(item_type_menu_title, item_type_menu_items)
        item_type_choice = item_type_menu.show()

        if item_type_choice == 0:
            add_item_type_prompt()

        elif item_type_choice == 1:
            remove_item_type_prompt()

        elif item_type_choice == 2:
            edit_item_type_prompt()

        elif item_type_choice == 3:
            break