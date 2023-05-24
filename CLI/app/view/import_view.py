# controllers.py

from model.currency_conversions import convert_to_copper
from controller.handle_item import ItemHandler
from controller.handle_item_type import ItemTypeHandler
from controller.handle_shop import ShopHandler
from controller.handle_shop_type import ShopTypeHandler
from controller.handle_city import CityHandler
from controller.handle_kingdom import KingdomHandler
from view.select_view import select_kingdom, select_city, select_shop, select_shop_type, basic_menu
from termcolor import colored
import csv
import os

def manage_import(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_handler = ShopHandler()
    item_handler = ItemHandler()
    item_type_handler = ItemTypeHandler()
    shop_type_handler = ShopTypeHandler()

    # Ask user if they want to add to a new shop or an existing one
    options = ["Add to new shop", "Add to existing shop", "Go back"]
    option_menu = basic_menu("Select an option:", options)
    selected_option_index = option_menu.show()

    selected_shop = None
    if selected_option_index == 0:  # Add to new shop
        # Select a Kingdom
        selected_kingdom = select_kingdom(session, kingdom_handler)
        if selected_kingdom is None:
            return

        # Select a City
        selected_city = select_city(session, city_handler, selected_kingdom.id)
        if selected_city is None:
            return

        # Select or Add a Shop Type
        shop_types = shop_type_handler.select_all(session)
        shop_type_names = [shop_type.name for shop_type in shop_types] + ["Add new shop type"]

        shop_type_menu = basic_menu("Select a Shop Type:", shop_type_names)
        selected_shop_type_index = shop_type_menu.show()

        # If user selected "Add new shop type"
        if selected_shop_type_index == len(shop_types):
            # Enter Shop Type Name
            shop_type_name = input(colored("Enter the new shop type name: ", attrs=['bold']))

            # Add the new shop type
            shop_type_handler.add(session, shop_type_name)
            print(colored("Shop type added successfully!", 'green'))

            # Fetch the new shop type
            selected_shop_type = shop_type_handler.select(session, shop_type_name)

        else:
            selected_shop_type = shop_types[selected_shop_type_index]

        if selected_shop_type is None:
            return

        # Enter Shop Name
        shop_name = input(colored("Enter the shop name: ", attrs=['bold']))

        # Add the shop
        shop_handler.add(session, shop_name, selected_shop_type.id, selected_city.id)
        print(colored("Shop added successfully!", 'green'))
        
        selected_shop = shop_handler.select(session, shop_name)
        
    elif selected_option_index == 1:  # Add to existing shop
        selected_kingdom = select_kingdom(session, kingdom_handler)
        if selected_kingdom is None:
            return
        
        selected_city = select_city(session, city_handler, selected_kingdom.id)
        if selected_city is None:
            return

        selected_shop = select_shop(session, shop_handler, selected_city.id)
        if selected_shop is None:
            return
    elif selected_option_index == 2:
        return

    # Retrieve created or selected shop
    if selected_shop is None:
        print(colored("Could not fetch shop.", "red"))
        return


    # List CSV files in the data/import directory
    directory = "data/import"
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    if not files:
        print(colored("No CSV files found in the data/import directory.", "red"))
        return

    # Prompt for CSV file
    file_menu = basic_menu(colored("Select a CSV file to import:", "bold"), files)
    selected_file_index = file_menu.show()
    csv_file_path = os.path.join(directory, files[selected_file_index])

    # Read the CSV file
    with open(csv_file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            # Get or create the item type
            item_type_name, item_sub_type = row['item type'].split(';')
            item_type = item_type_handler.select(session, item_type_name)

            if item_type is None:  # Item type does not exist, create it
                min_amount = float(input(colored(f"Enter the minimum amount for {item_type_name} items: ", "bold")))
                max_amount = float(input(colored(f"Enter the maximum amount for {item_type_name} items: ", "bold")))
                wealth_indicator = float(input(colored(f"Enter the wealth indicator for {item_type_name} items: ", "bold")))
                item_type_handler.add(session, item_type_name, item_sub_type, min_amount, max_amount, wealth_indicator)
                item_type = item_type_handler.select(session, item_type_name)

            # Convert prices to copper
            current_price_copper = convert_to_copper(row['current price'])
            min_price_copper = convert_to_copper(row['minimum price'])
            max_price_copper = convert_to_copper(row['maximum price'])

            # Add the item
            item_handler.add(
                session,
                item_name=row['item name'],
                current_price=current_price_copper,
                min_price=min_price_copper,
                max_price=max_price_copper,
                current_amount=row['current amount'],
                item_type_id=item_type.id,
                shop_id=selected_shop.id
            )

    # Remove the CSV file
    os.remove(csv_file_path)

    print(colored("Items imported successfully!", "green"))
