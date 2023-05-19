from library import *
from optionsDatabase import *

import os
import sqlite3
from termcolor import colored
from simple_term_menu import TerminalMenu

def import_item_list():
	import_folder = 'import'
	import_files = [f for f in os.listdir(import_folder) if f.endswith('.csv')]

	if not import_files:
		print("No CSV files found in the import directory.")
		return

	menu_title = "Choose CSV File to Import:"
	menu_items = [f[:-4] for f in import_files]
	menu = create_menu(menu_title, menu_items)
	file_index = menu.show()

	file_name = import_files[file_index]
	file_path = os.path.join(import_folder, file_name)

	with open(file_path, 'r') as file:
		reader = csv.DictReader(file)

		# Read the column names
		field_names = reader.fieldnames

		# Check if the required columns exist
		required_columns = ['item names', 'minimum price', 'maximum price', 'item type']
		missing_columns = [col for col in required_columns if col not in field_names]
		if missing_columns:
			print("Invalid file structure. Missing columns: ", ", ".join(missing_columns))
			return

		# Prompt for country, city, and shop information
		countries = get_countries()
		if not countries:
			print(colored("No countries found.", color='red', attrs=['bold']))
			return
		country_id = select_country(countries)

		cities = get_cities(country_id)
		if not cities:
			print(colored("No cities found.", color='red', attrs=['bold']))
			return
		city_id = select_city(cities)
		name = input(colored("Enter shop name: ", attrs=['bold']))
		shop_id = add_shop(name, city_id)  # Obtain the shop_id

		# Read and process the items
		for row in reader:
			item_name = row['item names']
			min_price = convert_currency_to_copper(row['minimum price'])
			max_price = convert_currency_to_copper(row['maximum price'])
			item_type = row['item type']

			# Check if the item type exists
			item_type_id = get_item_type_id(item_type)

			# If the item type doesn't exist, prompt the user to create a new one
			if item_type_id is None:
				print(f"Item type '{item_type}' does not exist. Creating a new item type.")

				size = input(colored("Enter item type size: ", attrs=['bold']))
				wealth_factor = int(input(colored("Enter item type wealth factor (1-10): ", attrs=['bold'])))
				min_amount = int(input(colored("Enter item type minimum amount: ", attrs=['bold'])))
				max_amount = int(input(colored("Enter item type maximum amount: ", attrs=['bold'])))

				item_type_id = add_item_type(item_type, size, wealth_factor, min_amount, max_amount)

			# Add the item to the shop
			add_item(item_name, min_price, max_price, shop_id, item_type_id)

	# Delete the imported file
	os.remove(file_path)

	print(colored("Item list imported successfully.", color='green', attrs=['bold']))


def export_item_list():
	
	countries = get_countries()
	if not countries:
		print(colored("No countries found.", color='red', attrs=['bold']))
		return

	country_id = select_country(countries)

	cities = get_cities(country_id)
	if not cities:
		print(colored("No cities found.", color='red', attrs=['bold']))
		return

	city_id = select_city(cities)

	shops = get_shops(city_id)
	if not shops:
		print(colored("No shops found.", color='red', attrs=['bold']))
		return

	shop_id = select_shop(shops)

	# Generate the filename with version number
	version = 1
	file_name = f"{country_name}_{city_name}_{shop_name}"
	while os.path.exists(f"export/{file_name}_v{version}.csv"):
		version += 1
	file_path = f"export/{file_name}_v{version}.csv"

	with open(file_path, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['item names', 'minimum price', 'maximum price', 'stock', 'item type'])

		items = get_items_by_shop(shop_id)
		for item in items:
			item_type = get_item_type(item[5])

			writer.writerow([item[1], item[2], item[3], item[4], item_type])

	print(colored("Item list exported successfully.", color='green', attrs=['bold']))