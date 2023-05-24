# view/shop_view.py
from controller.handle_kingdom import KingdomHandler
from controller.handle_city import CityHandler
from controller.handle_shop_type import ShopTypeHandler
from controller.handle_shop import ShopHandler
from .select_view import select_kingdom, select_city, select_shop, select_shop_type, basic_menu, clear_terminal
from termcolor import colored


def manage_shop(session):
    while True:
        manage_menu_entries = ["Add Shop", "Update Shop", "Delete Shop", "Show Shops", "Go back"]
        manage_menu = basic_menu("Manage Shop", manage_menu_entries)
        manage_menu_choice = manage_menu.show()
        clear_terminal()

        if manage_menu_choice == 0:  # "Add Shop"
            add_shop_view(session)

        elif manage_menu_choice == 1:  # "Update Shop"
            update_shop_view(session)

        elif manage_menu_choice == 2:  # "Delete Shop"
            delete_shop_view(session)

        elif manage_menu_choice == 3:  # "Show Shops"
            show_all_in_city_view(session)

        elif manage_menu_choice == 4:  # "Go back"
            break


def add_shop_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_type_handler = ShopTypeHandler()
    shop_handler = ShopHandler()

	# Select a Kingdom
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return

    # Select a City
    selected_city = select_city(session, city_handler, selected_kingdom.id)
    if selected_city is None:
        return

    # Select a Shop Type
    selected_shop_type = select_shop_type(session, shop_type_handler)
    if selected_shop_type is None:
        return

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
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return

    # Select a City
    selected_city = select_city(session, city_handler, selected_kingdom.id)
    if selected_city is None:
        return

    # Select a Shop
    selected_shop = select_shop(session, shop_handler, selected_city.id)
    if selected_shop is None:
        return

    # Choose whether to update shop details or migrate the shop
    action_menu = basic_menu("Choose an action:", ["Update Shop Details", "Migrate Shop"])
    selected_action_index = action_menu.show()

    if selected_action_index == 0:  # User selected "Update Shop Details"
        # Enter new Shop Name
        new_shop_name = input("Enter the new shop name: ")

        # Select a Shop Type
        selected_shop_type = select_shop_type(session, shop_type_handler)
        if selected_shop_type is None:
            return

        # Update the shop
        shop_handler.update(session, selected_shop.id, new_shop_name, selected_shop_type.id, selected_shop.city.id)
    else:  # User selected "Migrate Shop"
        migrate_shop_view(session, selected_shop)

    # Update the shop
    print(colored("Shop updated successfully!", 'green'))


def migrate_shop_view(session, selected_shop):
    # Create handlers
    shop_handler = ShopHandler()
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

    # Migrate the shop
    shop_handler.update(session, selected_shop.id, selected_shop.name, selected_shop.shop_type_id, selected_city.id)
    print(colored("Shop migrated successfully!", 'green'))


def delete_shop_view(session):
    # Create handler
    shop_handler = ShopHandler()
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

    # Select a Shop
    selected_shop = select_shop(session, shop_handler, selected_city.id)
    if selected_shop is None:
        return

    # Confirm deletion
    confirmation_menu = basic_menu("Are you sure you want to delete this shop?", ["Yes", "No"])
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
    selected_kingdom = select_kingdom(session, kingdom_handler)
    if selected_kingdom is None:
        return

    # Select a City
    selected_city = select_city(session, city_handler, selected_kingdom.id)
    if selected_city is None:
        return

    # Show all shops in the selected city
    shops = shop_handler.select_by_city(session, selected_city.id)
    if shops is None:
        return

    for shop in shops:
        print(shop)