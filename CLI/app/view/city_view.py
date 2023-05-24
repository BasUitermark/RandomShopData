# view/city_view.py
from controller.handle_kingdom import KingdomHandler
from controller.handle_city import CityHandler
from .select_view import select_city, select_kingdom, basic_menu, clear_terminal
from termcolor import colored


def manage_city(session):
    while True:
        manage_menu_entries = ["Add City", "Update City", "Delete City", "Show Citiess", "Go back"]
        manage_menu = basic_menu("Manage City", manage_menu_entries)
        manage_menu_choice = manage_menu.show()
        clear_terminal()

        if manage_menu_choice == 0:  # "Add City"
            add_city_view(session)

        elif manage_menu_choice == 1:  # "Update City"
            update_city_view(session)

        elif manage_menu_choice == 2:  # "Delete City"
            delete_city_view(session)

        elif manage_menu_choice == 3:  # "Show Citys"
            show_all_in_kingdom_view(session)

        elif manage_menu_choice == 4:  # "Go back"
            break


def add_city_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()

    # Select a Kingdom
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return

    # Enter name & population
    city_name = input(colored("Enter the city name: ", attrs=['bold']))
    city_population = input(colored("Enter the city population: ", attrs=['bold']))
    city_wealth = input(colored("Enter the city wealth factor: ", attrs=['bold']))

    # Add the city
    city_handler.add(session, city_name, city_population, city_wealth, selected_kingdom.id)
    print(colored("Shop added successfully!", 'green'))


def update_city_view(session):
    # Create handlers
    city_handler = CityHandler()
    kingdom_handler = KingdomHandler()

	# Select a Kingdom
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return

    # Select a City
    selected_city = select_city(session, city_handler, selected_kingdom.id)
    if selected_city is None:
        return

    # Choose whether to update city details or migrate the city
    action_menu = basic_menu("Choose an action:", ["Update City Details", "Migrate City"])
    selected_action_index = action_menu.show()

    if selected_action_index == 0:  # User selected "Update City Details"
        # Enter new City Name
        new_city_name = input(colored("Enter the city name: ", attrs=['bold']))
        new_city_population = input(colored("Enter the city population: ", attrs=['bold']))

        # Update the city
        city_handler.update(session, selected_city.id, new_city_name, new_city_population, selected_city.kingdom.id)
        print(colored("City updated successfully!", 'green'))
    else:  # User selected "Migrate City"
        migrate_city_view(session, selected_city)

    # Update the city
    print(colored("City updated successfully!", 'green'))


def migrate_city_view(session, selected_city):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()

    # Select a new Kingdom
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return   

    # Migrate the city
    city_handler.update(session, selected_city.id, selected_city.name, selected_city.population, selected_kingdom.id)
    print(colored("City migrated successfully!", 'green'))


def delete_city_view(session):
    # Create handler
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()

	# Select a Kingdom
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return

    # Select a City
    selected_city = select_city(session, city_handler, selected_kingdom.id)
    if selected_city is None:
        return

    # Confirm deletion
    confirmation_menu = basic_menu("Are you sure you want to delete this city?", ["Yes", "No"])
    confirmation_index = confirmation_menu.show()

    if confirmation_index == 0:  # User selected "Yes"
        # Delete the city
        city_handler.delete(session, selected_city.id)
        print(colored("City deleted successfully!", 'green'))
    else:
        print(colored("City deletion cancelled.", 'yellow'))



def show_all_in_kingdom_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()

	# Select a Kingdom
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return

    # Show all citys in the selected kingdom
    citys = city_handler.select_by_kingdom(session, selected_kingdom.id)
    for city in citys:
        print(colored(city.name, 'light_green'))