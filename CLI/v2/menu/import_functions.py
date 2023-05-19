import os
import csv
from termcolor import colored
from database.database_operation import *
from .functions import create_menu, select_city_menu, select_country_menu, convert_currency_to_copper

def import_item_list():
    import_folder = 'import'
    import_files = [f for f in os.listdir(import_folder) if f.endswith('.csv')]

    if not import_files:
        print(colored("No CSV files found in the import directory.", color='red'))
        return

    file_name = select_csv_file(import_files)
    file_path = os.path.join(import_folder, file_name)

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        countries = select_country_menu()
        if not countries:
            print(colored("No countries found.", color='red'))
            return

        city = select_city_menu(countries.id)
        if not city:
            print(colored("No cities found.", color='red'))
            return

        shop_name = input(colored("Enter the name of the shop: ", attrs=['bold']))
        shop = add_shop(shop_name, city.id)
        print(f"Shop '{colored(shop.name, color='green', attrs=['bold'])}' added successfully.")

        process_items(reader, shop)

    # Delete the imported file
    os.remove(file_path)
    print(f"File '{colored(file_name, color='green', attrs=['bold'])}' imported and processed successfully.")

def select_csv_file(import_files):
    menu_title = "Choose CSV File to Import:"
    menu_items = [f[:-4] for f in import_files]
    menu = create_menu(menu_title, menu_items)
    file_index = menu.show()
    return import_files[file_index]

def process_items(reader, shop):
    for row in reader:
        item_name, current_price, min_price, max_price, current_amount, item_type = row

        # Convert currency values to copper (cp)
        current_price_cp = convert_currency_to_copper(current_price)
        min_price_cp = convert_currency_to_copper(min_price)
        max_price_cp = convert_currency_to_copper(max_price)

        item_type_name, item_type_subtype = parse_item_type(item_type)

        item_type = get_item_type_by_name(item_type_name, item_type_subtype)
        if not item_type:
            print(colored(f"Item type '{item_type_name}' - '{item_type_subtype}' doesn't exist. "
                          "Creating a new item type.", color='yellow'))

            wealth_factor = int(input(colored("Enter item type wealth factor (1-10): ", attrs=['bold'])))
            min_amount = int(input(colored("Enter item type minimum amount: ", attrs=['bold'])))
            max_amount = int(input(colored("Enter item type maximum amount: ", attrs=['bold'])))

            item_type = add_item_type(item_type_name, item_type_subtype, min_amount, max_amount, wealth_factor)
            print(colored(f"Item type '{item_type_name}' - '{item_type_subtype}' created successfully.", color='green'))

        if item_type is not None:
            added, error_message = add_item(item_name, current_price_cp, min_price_cp, max_price_cp,
                                            int(current_amount), item_type.id, shop.id)
            if added:
                print(f"Item '{colored(item_name, color='green', attrs=['bold'])}' added to "
                      f"'{colored(shop.name, color='green', attrs=['bold'])}' successfully.")
            else:
                print(colored(f"Failed to add item '{item_name}' to '{shop.name}'. "
                              f"Reason: {error_message}", color='red'))
        else:
            print(colored(f"Failed to add item '{item_name}' to '{shop.name}'. "
                          "Please check the item type details.", color='red'))





def parse_item_type(item_type):
    item_type_parts = item_type.split(";")
    if len(item_type_parts) != 2:
        print(colored(f"Invalid item type format: {item_type}. Using default values.", color='yellow'))
        return "Item", "Default"

    return item_type_parts[0].strip(), item_type_parts[1].strip()
