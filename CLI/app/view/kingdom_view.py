# view/kingdom_view.py
from controller.handle_kingdom import KingdomHandler
from terminal_menu import create_menu
from termcolor import colored


def add_kingdom_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()

    # Enter Kingdom Name
    kingdom_name = input(colored("Enter the kingdom name: ", attrs=['bold']))

    # Add the kingdom
    kingdom_handler.add(session, kingdom_name)
    print(colored("Shop added successfully!", 'green'))


def update_kingdom_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()

    # Select a Kingdom
    kingdoms = kingdom_handler.select_all(session)
    kingdom_menu = create_menu("Select a Shop to Update:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    # Enter new Shop Name
    new_kingdom_name = input("Enter the new kingdom name: ")

    # Update the kingdom
    kingdom_handler.update(session, selected_kingdom.id, new_kingdom_name)
    print("Shop updated successfully!")

    # Update the kingdom
    print("Shop updated successfully!")



def delete_kingdom_view(session):
    # Create handler
    kingdom_handler = KingdomHandler()

    # Select a Shop
    kingdoms = kingdom_handler.select_all(session)
    kingdom_menu = create_menu("Select a Kingdom to Delete:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    # Confirm deletion
    confirmation_menu = create_menu("Are you sure you want to delete this kingdom?", ["Yes", "No"])
    confirmation_index = confirmation_menu.show()

    if confirmation_index == 0:  # User selected "Yes"
        # Delete the kingdom
        kingdom_handler.delete(session, selected_kingdom.id)
        print("Shop deleted successfully!")
    else:
        print("Shop deletion cancelled.")



def show_all_in_city_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()

    # Select a Kingdom
    kingdoms = kingdom_handler.select_all(session)
    for kingdom in kingdoms:
        print(kingdom)