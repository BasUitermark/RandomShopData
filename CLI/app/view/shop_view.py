# view/shop_view.py
from controller.handle_kingdom import KingdomHandler
from controller.handle_city import CityHandler
from controller.handle_shop_type import ShopTypeHandler
from controller.handle_shop import ShopHandler
from terminal_menu import create_menu
from termcolor import colored


def add_shop_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_type_handler = ShopTypeHandler()
    shop_handler = ShopHandler()

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

    # Select a Shop Type
    shop_types = shop_type_handler.select_all(session)
    shop_type_menu = create_menu("Select a Shop Type:", [shop_type.name for shop_type in shop_types])
    selected_shop_type_index = shop_type_menu.show()
    selected_shop_type = shop_types[selected_shop_type_index]

    # Enter Shop Name
    shop_name = input(colored("Enter the shop name: ", attrs=['bold']))

    # Add the shop
    shop_handler.add(session, shop_name, selected_shop_type.id, selected_city.id)
    print(colored("Shop added successfully!", 'green'))


def update_shop_view(session):
    # Create handlers
    shop_handler = ShopHandler()
    shop_type_handler = ShopTypeHandler()
    city_handler = CityHandler()
    kingdom_handler = KingdomHandler()

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

    # Select a Shop
    shops = shop_handler.select_by_city(session, selected_city.id)
    shop_menu = create_menu("Select a Shop to Update:", [shop.name for shop in shops])
    selected_shop_index = shop_menu.show()
    selected_shop = shops[selected_shop_index]

    # Choose whether to update shop details or migrate the shop
    action_menu = create_menu("Choose an action:", ["Update Shop Details", "Migrate Shop"])
    selected_action_index = action_menu.show()

    if selected_action_index == 0:  # User selected "Update Shop Details"
        # Enter new Shop Name
        new_shop_name = input("Enter the new shop name: ")

        # Select a new Shop Type
        shop_types = shop_type_handler.select_all(session)
        shop_type_menu = create_menu("Select a new Shop Type:", [shop_type.name for shop_type in shop_types])
        selected_shop_type_index = shop_type_menu.show()
        selected_shop_type = shop_types[selected_shop_type_index]

        # Update the shop
        shop_handler.update(session, selected_shop.id, new_shop_name, selected_shop_type.id, selected_shop.city.id)
        print("Shop updated successfully!")
    else:  # User selected "Migrate Shop"
        migrate_shop_view(session, selected_shop)

    # Update the shop
    print("Shop updated successfully!")


def migrate_shop_view(session, selected_shop):
    # Create handlers
    shop_handler = ShopHandler()
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()

    # Select a new Kingdom
    kingdoms = kingdom_handler.select_all(session)
    kingdom_menu = create_menu("Select a new Kingdom:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    # Select a new City within the selected Kingdom
    cities = city_handler.select_by_kingdom(session, selected_kingdom.id)
    city_menu = create_menu("Select a new City in the selected Kingdom:", [city.name for city in cities])
    selected_city_index = city_menu.show()
    selected_city = cities[selected_city_index]

    # Migrate the shop
    shop_handler.update(session, selected_shop.id, selected_shop.name, selected_shop.shop_type_id, selected_city.id)
    print(colored("Shop migrated successfully!", 'green'))


def delete_shop_view(session):
    # Create handler
    shop_handler = ShopHandler()

    # Select a Shop
    shops = shop_handler.select_all(session)
    shop_menu = create_menu("Select a Shop to Delete:", [shop.name for shop in shops])
    selected_shop_index = shop_menu.show()
    selected_shop = shops[selected_shop_index]

    # Confirm deletion
    confirmation_menu = create_menu("Are you sure you want to delete this shop?", ["Yes", "No"])
    confirmation_index = confirmation_menu.show()

    if confirmation_index == 0:  # User selected "Yes"
        # Delete the shop
        shop_handler.delete(session, selected_shop.id)
        print("Shop deleted successfully!")
    else:
        print("Shop deletion cancelled.")



def show_all_in_city_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_handler = ShopHandler()

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

    # Show all shops in the selected city
    shops = shop_handler.select_by_city(session, selected_city.id)
    for shop in shops:
        print(shop)