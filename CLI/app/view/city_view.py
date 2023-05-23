# view/city_view.py
from controller.handle_kingdom import KingdomHandler
from controller.handle_city import CityHandler
from terminal_menu import create_menu
from termcolor import colored


def add_city_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()

    # Select a Kingdom
    kingdoms = kingdom_handler.select_all(session)
    kingdom_menu = create_menu("Select a Kingdom:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    # Select a City
    cities = city_handler.select_by_kingdom(session, selected_kingdom.id)
    city_menu = create_menu("Select a City:", [city.name for city in cities])
    selected_city_index = city_menu.show()
    selected_city = cities[selected_city_index]

    # Enter Shop Name
    city_name = input(colored("Enter the city name: ", attrs=['bold']))
    city_population = input(colored("Enter the city population: ", attrs=['bold']))

    # Add the city
    city_handler.add(session, city_name, city_population, selected_city.id)
    print(colored("Shop added successfully!", 'green'))


def update_city_view(session):
    # Create handlers
    city_handler = CityHandler()
    kingdom_handler = KingdomHandler()

	# Select a Kingdom
    kingdoms = kingdom_handler.select_all(session)
    kingdom_menu = create_menu("Select a Kingdom:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    # Select a City
    citys = city_handler.select_by_kingdom(session, selected_kingdom.id)
    city_menu = create_menu("Select a City to Update:", [city.name for city in citys])
    selected_city_index = city_menu.show()
    selected_city = citys[selected_city_index]

    # Choose whether to update city details or migrate the city
    action_menu = create_menu("Choose an action:", ["Update City Details", "Migrate City"])
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
    kingdoms = kingdom_handler.select_all(session)
    kingdom_menu = create_menu("Select a new Kingdom:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    # Migrate the city
    city_handler.update(session, selected_city.id, selected_city.name, selected_city.population, selected_kingdom.id)
    print(colored("Shop migrated successfully!", 'green'))


def delete_city_view(session):
    # Create handler
    city_handler = CityHandler()

    # Select a Shop
    citys = city_handler.select_all(session)
    city_menu = create_menu("Select a Shop to Delete:", [city.name for city in citys])
    selected_city_index = city_menu.show()
    selected_city = citys[selected_city_index]

    # Confirm deletion
    confirmation_menu = create_menu("Are you sure you want to delete this city?", ["Yes", "No"])
    confirmation_index = confirmation_menu.show()

    if confirmation_index == 0:  # User selected "Yes"
        # Delete the city
        city_handler.delete(session, selected_city.id)
        print("Shop deleted successfully!")
    else:
        print("Shop deletion cancelled.")



def show_all_in_city_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()

    # Select a Kingdom
    kingdoms = kingdom_handler.select_all(session)
    kingdom_menu = create_menu("Select a Kingdom:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    # Show all citys in the selected kingdom
    citys = city_handler.select_by_kingdom(session, selected_kingdom.id)
    for city in citys:
        print(city)