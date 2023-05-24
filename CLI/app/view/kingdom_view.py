# view/kingdom_view.py
from controller.handle_kingdom import KingdomHandler
from .select_view import select_kingdom, basic_menu, clear_terminal
from termcolor import colored


def manage_kingdom(session):
    while True:
        manage_menu_entries = ["Add Kingdom", "Update Kingdom", "Delete Kingdom", "Show Kingdoms", "Go back"]
        manage_menu = basic_menu("Manage Kingdom", manage_menu_entries)
        manage_menu_choice = manage_menu.show()
        clear_terminal()

        if manage_menu_choice == 0:  # "Add Kingdom"
            add_kingdom_view(session)

        elif manage_menu_choice == 1:  # "Update Kingdom"
            update_kingdom_view(session)

        elif manage_menu_choice == 2:  # "Delete Kingdom"
            delete_kingdom_view(session)

        elif manage_menu_choice == 3:  # "Show Kingdoms"
            show_all_kingdoms(session)

        elif manage_menu_choice == 4:  # "Go back"
            break


def add_kingdom_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()

    # Enter Kingdom Name
    kingdom_name = input(colored("Enter the kingdom name: ", attrs=['bold']))

    # Add the kingdom
    kingdom_handler.add(session, kingdom_name)
    print(colored("Kingdom added successfully!", 'green'))


def update_kingdom_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()

    # Select a Kingdom
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return

    # Enter new Kingdom Name
    new_kingdom_name = input("Enter the new kingdom name: ")

    # Update the kingdom
    kingdom_handler.update(session, selected_kingdom.id, new_kingdom_name)
    print(colored("Kingdom updated successfully!", 'green'))



def delete_kingdom_view(session):
    # Create handler
    kingdom_handler = KingdomHandler()

    # Select a Kingdom
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return

    # Confirm deletion
    confirmation_menu = basic_menu("Are you sure you want to delete this kingdom?", ["Yes", "No"])
    confirmation_index = confirmation_menu.show()

    if confirmation_index == 0:  # User selected "Yes"
        # Delete the kingdom
        kingdom_handler.delete(session, selected_kingdom.id)
        print(colored("Kingdom deleted successfully!", 'green'))
    else:
        print(colored("Kingdom deletion cancelled.", 'yellow'))



def show_all_kingdoms(session):
    # Create handlers
    kingdom_handler = KingdomHandler()

    # Select a Kingdom
    kingdoms = kingdom_handler.select_all(session)
    if kingdoms is None:
        print(colored("No kingdoms found.", 'yellow'))
        return

    for kingdom in kingdoms:
        print(colored(kingdom.name, 'light_green'))