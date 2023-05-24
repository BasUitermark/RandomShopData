# view/shop_type_view.py
from controller.handle_shop_type import ShopTypeHandler
from .select_view import select_shop_type, basic_menu, clear_terminal
from termcolor import colored


def manage_shop_type(session):
    while True:
        manage_menu_entries = ["Add Shop Type", "Update Shop Type", "Delete Shop Type", "Show Shop Types", "Go back"]
        manage_menu = basic_menu("Manage Shop Type", manage_menu_entries)
        manage_menu_choice = manage_menu.show()
        clear_terminal()

        if manage_menu_choice == 0:  # "Add Shop Type"
            add_shop_type_view(session)

        elif manage_menu_choice == 1:  # "Update Shop Type"
            update_shop_type_view(session)

        elif manage_menu_choice == 2:  # "Delete Shop Type"
            delete_shop_type_view(session)

        elif manage_menu_choice == 3:  # "Show Shop Types"
            show_all_shop_types_view(session)

        elif manage_menu_choice == 4:  # "Go back"
            break


def add_shop_type_view(session):
    # Create handlers
    shop_type_handler = ShopTypeHandler()

    # Enter Shop Type details
    shop_type_name = input(colored("Enter the shop type name: ", attrs=['bold']))

    # Add the shop type
    shop_type_handler.add(session, shop_type_name)
    print(colored("Shop Type added successfully!", 'green'))


def update_shop_type_view(session):
    # Create handlers
    shop_type_handler = ShopTypeHandler()

    # Select a Shop Type
    selected_shop_type = select_shop_type(session, shop_type_handler)
    if selected_shop_type is None:
        return

    # Enter new Shop Type details
    new_shop_type_name = input("Enter the new shop type name: ")

    # Update the shop type
    shop_type_handler.update(session, selected_shop_type.id, new_shop_type_name)
    print(colored("Shop Type updated successfully!", 'green'))


def delete_shop_type_view(session):
    # Create handler
    shop_type_handler = ShopTypeHandler()

    # Select a Shop Type
    selected_shop_type = select_shop_type(session, shop_type_handler)
    if selected_shop_type is None:
        return

    # Confirm deletion
    confirmation_menu = basic_menu("Are you sure you want to delete this shop type?", ["Yes", "No"])
    confirmation_index = confirmation_menu.show()

    if confirmation_index == 0:  # User selected "Yes"
        # Delete the shop type
        shop_type_handler.delete(session, selected_shop_type.id)
        print(colored("Shop Type deleted successfully!", 'green'))


def show_all_shop_types_view(session):
    # Create handler
    shop_type_handler = ShopTypeHandler()

    # Get and print all shop types
    all_shop_types = shop_type_handler.select_all(session)
    if all_shop_types is None:
        return

    for shop_type in all_shop_types:
        print(shop_type)
