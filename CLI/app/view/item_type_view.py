# view/item_type_view.py
from controller.handle_item_type import ItemTypeHandler
from .select_view import select_item_type, basic_menu, clear_terminal
from termcolor import colored


def manage_item_type(session):
    global breadcrumbs
    while True:
        manage_menu_entries = ["Add Item Type", "Update Item Type", "Delete Item Type", "Show Item Types", "Go back"]
        manage_menu = basic_menu("Manage Item Type", manage_menu_entries)
        manage_menu_choice = manage_menu.show()
        clear_terminal()

        if manage_menu_choice == 0:  # "Add Item Type"
            breadcrumbs.append("Add Item Type")
            add_item_type_view(session)
            breadcrumbs = breadcrumbs[:-1]

        elif manage_menu_choice == 1:  # "Update Item Type"
            breadcrumbs.append("Update Item Type")
            update_item_type_view(session)
            breadcrumbs = breadcrumbs[:-1]

        elif manage_menu_choice == 2:  # "Delete Item Type"
            breadcrumbs.append("Delete Item Type")
            delete_item_type_view(session)
            breadcrumbs = breadcrumbs[:-1]

        elif manage_menu_choice == 3:  # "Show Item Types"
            breadcrumbs.append("Show Item Types")
            show_all_item_types_view(session)
            breadcrumbs = breadcrumbs[:-1]

        elif manage_menu_choice == 4:  # "Go back"
            break


def add_item_type_view(session):
    # Create handlers
    item_type_handler = ItemTypeHandler()

    # Enter Item Type details
    item_type_name = input(colored("Enter the item type name: ", attrs=['bold']))
    sub_type = input(colored("Enter the sub type: ", attrs=['bold']))
    min_amount = input(colored("Enter the minimum amount: ", attrs=['bold']))
    max_amount = input(colored("Enter the maximum amount: ", attrs=['bold']))
    wealth_indicator = input(colored("Enter the wealth indicator: ", attrs=['bold']))

    # Add the item type
    item_type_handler.add(session, item_type_name, sub_type, min_amount, max_amount, wealth_indicator)
    print(colored("Item Type added successfully!", 'green'))


def update_item_type_view(session):
    # Create handlers
    item_type_handler = ItemTypeHandler()

    # Select an Item Type
    selected_item_type = select_item_type(session, item_type_handler)
    if selected_item_type is None:
        return

    while True:
        # Choose the attribute to update
        attribute_menu = basic_menu("Choose an attribute to update:", ["Item Type", "Sub Type", "Min Amount", "Max Amount", "Wealth Indicator", "Go back"])
        selected_attribute_index = attribute_menu.show()
        new_value = None

        if selected_attribute_index == 0:  # User selected "Item Type"
            new_value = input(colored("Enter the new item type: ", attrs=['bold']))
            item_type_handler.update(session, selected_item_type.id, item_type=new_value)
        elif selected_attribute_index == 1:  # User selected "Sub Type"
            new_value = input(colored("Enter the new sub type: ", attrs=['bold']))
            item_type_handler.update(session, selected_item_type.id, sub_type=new_value)
        elif selected_attribute_index == 2:  # User selected "Min Amount"
            new_value = input(colored("Enter the new min amount: ", attrs=['bold']))
            item_type_handler.update(session, selected_item_type.id, min_amount=new_value)
        elif selected_attribute_index == 3:  # User selected "Max Amount"
            new_value = input(colored("Enter the new max amount: ", attrs=['bold']))
            item_type_handler.update(session, selected_item_type.id, max_amount=new_value)
        elif selected_attribute_index == 4:  # User selected "Wealth Indicator"
            new_value = input(colored("Enter the new wealth indicator: ", attrs=['bold']))
            item_type_handler.update(session, selected_item_type.id, wealth_indicator=new_value)
        elif selected_attribute_index == 5:  # "Go back"
            break

    print(colored("Item Type updated successfully!", 'green'))


def delete_item_type_view(session):
    # Create handler
    item_type_handler = ItemTypeHandler()

    # Select an Item Type
    selected_item_type = select_item_type(session, item_type_handler)
    if selected_item_type is None:
        return

    # Confirm deletion
    confirmation_menu = basic_menu("Are you sure you want to delete this item type?", ["Yes", "No"])
    confirmation_index = confirmation_menu.show()

    if confirmation_index == 0:  # User selected "Yes"
        # Delete the item type
        item_type_handler.delete(session, selected_item_type.id)
        print(colored("Item Type deleted successfully!", 'green'))


def show_all_item_types_view(session):
    # Create handler
    item_type_handler = ItemTypeHandler()

    # Get and print all item types
    all_item_types = item_type_handler.select_all(session)
    if all_item_types is None:
        return
    for item_type in all_item_types:
        print(item_type)
