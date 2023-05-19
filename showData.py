from optionsDatabase import *
from library import *

import pandas as pd

def show_tables_menu():
	select_menu_titel = "Select an option"
	select_menu_items = ["Show Countries", "Show Cities", "Show Shops", "Show Items", "Back"]
	select_menu = create_menu(select_menu_titel, select_menu_items)
	
	index = select_menu.show()
	if index == 0:
		generate_country_table()
	elif index == 1:
		generate_country_city_table()
	elif index == 2:
		generate_shops_in_cities_table()
	elif index == 3:
		generate_items_in_shops_table()
	elif index == 4:
		return

def generate_country_table():
	countries = get_countries()

	# Create an empty DataFrame
	table = pd.DataFrame()

	# Add countries as column names
	for country_id, country_name in countries:
		table[country_name] = ''

	# Fill NaN values with empty string
	table.fillna('', inplace=True)

	# Sort the DataFrame by column names
	table.sort_index(axis=1, inplace=True)

	print(table)

def generate_shops_in_cities_table():
	countries = get_countries()

	country_id = select_country(countries)
	if not country_id:
		print(colored("No countries found.", color='red', attrs=['bold']))
	cities = get_cities()
 
	city_id = select_city(cities)
	if not city_id:
		print(colored("No cities found.", color='red', attrs=['bold']))
	shops = get_shops(city_id)
	shop_id = select_shop(shops)
	if not shop_id:
		print(colored("No shops found.", color='red', attrs=['bold']))

	# Create an empty DataFrame
	table = pd.DataFrame()

	# Add cities as column names
	for city_id, city_name, country_id in cities:
		table[city_name] = ''

	# Add shops as values below cities
	for shop_id, shop_name, city_id in shops:
		city_name = get_city_name(city_id)
		table.loc[shop_name, city_name] = shop_name

	# Fill NaN values with empty string
	table.fillna('', inplace=True)

	# Sort the DataFrame by column names
	table.sort_index(axis=1, inplace=True)

	print(table)
	
def generate_items_in_shops_table():
	countries = get_countries()

	country_id = select_country(countries)
	if not country_id:
		print(colored("No countries found.", color='red', attrs=['bold']))
		return

	cities = get_cities(country_id)

	city_id = select_city(cities)
	if not city_id:
		print(colored("No cities found.", color='red', attrs=['bold']))
		return

	shops = get_shops(city_id)
	shop_id = select_shop(shops)
	if not shop_id:
		print(colored("No shops found.", color='red', attrs=['bold']))
		return

	items = get_items(shop_id)
	if not items:
		print(colored("No items found in the selected shop.", color='red', attrs=['bold']))
		return

	item_types = get_item_types()

	print(items)

	# Create an empty DataFrame
	table = pd.DataFrame(columns=['Item Name', 'Minimum Price', 'Maximum Price', 'Item Type'])

	# Add items in shops
	for item_id, item_name, item_type_id, min_price, max_price in items:
		item_type = get_item_type_name(item_type_id)
		if item_type is not None:
			table = table.append({
				'Item Name': item_name,
				'Minimum Price': min_price,
				'Maximum Price': max_price,
				'Item Type': item_type
			}, ignore_index=True)

	# Fill NaN values with empty string
	table.fillna('', inplace=True)

	print(table)