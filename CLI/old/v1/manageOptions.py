from library import *
from optionsDatabase import *

import sqlite3
from simple_term_menu import TerminalMenu
from termcolor import colored

def manage_countries():
	while True:
		menu_title = "Manage Countries"
		menu_items = ["Add Country", "Remove Country", "Back"]
		menu = basic_menu(menu_title, menu_items)
		index = menu.show()

		if index == 0:
			name = input(colored("Enter country name: ", attrs=['bold']))
			add_country(name)
		elif index == 1:
			countries = get_countries()
			if not countries:
				print(colored("No countries found.", color='red', attrs=['bold']))
				break
			country_menu_title = "Select country to remove:"
			country_menu_items = [country[1] for country in countries]
			country_menu = basic_menu(country_menu_title, country_menu_items)
			country_index = country_menu.show()
			country_id = countries[country_index][0]
			remove_country(country_id)
		elif index == 2:
			break

def manage_cities():
	while True:
		countries = get_countries()
		if not countries:
			print(colored("No countries found.", color='red', attrs=['bold']))
			break
		country_id = select_country(countries)
		if not country_id:
			break

		select_menu_title = "Select an option"
		select_menu_items = ["Add City", "Remove City", "Edit City", "Back"]
		menu = basic_menu(select_menu_title, select_menu_items)
		index = menu.show()

		if index == 0:
			name = input(colored("Enter city name: ", attrs=['bold']))
			population = int(input(colored("Enter city population: ", attrs=['bold'])))
			wealth_factor = int(input(colored("Enter city wealth factor (1-10): ", attrs=['bold'])))
			add_city(name, population, wealth_factor, country_id)
		elif index == 1:
			cities = get_cities(country_id)
			if not cities:
				print(colored("No cities found.", color='red', attrs=['bold']))
				break

			city_id = select_city(cities)
			if not country_id:
				break
			remove_city(city_id)
		elif index == 2:
			cities = get_cities(country_id)
			if not cities:
				print(colored("No cities found.", color='red', attrs=['bold']))
				break

			while True:
				city_menu_title = "Select city to edit (Back to go back)"
				city_menu_items = [city[1] for city in cities]
				city_menu = basic_menu(city_menu_title, city_menu_items)
				city_index = city_menu.show()

				if city_index == len(city_menu_items):
					break

				city_id = cities[city_index][0]
				city_name = cities[city_index][1]
				city_population = cities[city_index][2]
				city_wealth_factor = cities[city_index][3]

				edit_menu_title = f"Edit {city_name}"
				edit_menu_items = [
					f"Edit Name (Current: {city_name})",
					f"Edit Population (Current: {city_population})",
					f"Edit Wealth Factor (Current: {city_wealth_factor})",
					"Back"
				]
				edit_menu = basic_menu(edit_menu_title, edit_menu_items)
				edit_index = edit_menu.show()

				if edit_index == 0:
					new_name = input(colored("Enter new city name: ", attrs=['bold']))
					update_city_name(city_id, new_name)
				elif edit_index == 1:
					new_population = int(input(colored("Enter new city population: ", attrs=['bold'])))
					update_city_population(city_id, new_population)
				elif edit_index == 2:
					new_wealth_factor = int(input(colored("Enter new city wealth factor (1-10): ", attrs=['bold'])))
					update_city_wealth_factor(city_id, new_wealth_factor)
				elif edit_index == 3:
					break

		elif index == 3:
			break

def manage_shops():
    while True:
        select_menu_title = "Select an option"
        select_menu_items = ["Add Shop", "Remove Shop", "Edit Shop", "Back"]
        menu = basic_menu(select_menu_title, select_menu_items)
        index = menu.show()

        if index == 0:
            city_id = int(input(colored("Enter city ID where the shop belongs: ", attrs=['bold'])))
            shop_name = input(colored("Enter shop name: ", attrs=['bold']))

            conn = sqlite3.connect('mydatabase.sqlite')
            c = conn.cursor()

            c.execute("INSERT INTO shops (city_id, name) VALUES (?, ?)", (city_id, shop_name))

            conn.commit()
            conn.close()
        elif index == 1:
            countries = get_countries()
            country_id = select_country(countries)
            if not country_id:
                print(colored("No countries found.", color='red', attrs=['bold']))
            cities = get_cities(country_id)
            city_id = select_city(cities)
            if not city_id:
                print(colored("No cities found.", color='red', attrs=['bold']))
            shops = get_shops(city_id)

            if shops:
                print(colored("Select shop to remove:", attrs=['bold']))
                shop_menu_items = [shop[1] for shop in shops]  # Assuming shop name is at index 1
                shop_menu = basic_menu("Shop Menu", shop_menu_items)
                shop_index = shop_menu.show()
                shop_id = shops[shop_index][0]

                conn = sqlite3.connect('mydatabase.sqlite')
                c = conn.cursor()

                c.execute("DELETE FROM shops WHERE id=?", (shop_id,))

                conn.commit()
                conn.close()
            else:
                print(colored("No shops found.", color='red', attrs=['bold']))
        elif index == 2:
            conn = sqlite3.connect('mydatabase.sqlite')
            c = conn.cursor()

            c.execute("SELECT * FROM shops")
            shops = c.fetchall()

            conn.close()

            if shops:
                print(colored("Select shop to edit:", attrs=['bold']))
                shop_menu_items = [shop[1] for shop in shops]  # Assuming shop name is at index 1
                shop_menu = basic_menu("Shop Menu", shop_menu_items)
                shop_index = shop_menu.show()
                shop_id = shops[shop_index][0]

                new_shop_name = input(colored("Enter new shop name (blank to skip): ", attrs=['bold']))

                conn = sqlite3.connect('mydatabase.sqlite')
                c = conn.cursor()

                update_query = "UPDATE shops SET "
                update_params = []
                if new_shop_name:
                    update_query += "name=?, "
                    update_params.append(new_shop_name)

                if not update_params:
                    print(colored("No changes made.", color='yellow', attrs=['bold']))
                else:
                    update_query = update_query.rstrip(", ") + " WHERE id=?"
                    update_params.append(shop_id)

                    c.execute(update_query, tuple(update_params))

                    conn.commit()
                    conn.close()

                    print(colored("Shop updated successfully.", color='green', attrs=['bold']))
            else:
                print(colored("No shops found.", color='red', attrs=['bold']))
        elif index == 3:
            break


def manage_items():
	while True:
		countries = get_countries()
		if not countries:
			print(colored("No countries found.", color='red', attrs=['bold']))
			break

		country_id = select_country(countries)
		if not country_id:
			break
		cities = get_cities(country_id)
		if not cities:
			print(colored("No cities found.", color='red', attrs=['bold']))
			break

		city_id = select_city(cities)
		if not city_id:
			break
		shops = get_shops(city_id)
		if not shops:
			print(colored("No shops found.", color='red', attrs=['bold']))
			break

		shop_id = select_shop(shops)
		if not shop_id:
			break
		items = get_items(shop_id)

		select_menu_title = "Select an option"
		select_menu_items = ["Add Item", "Remove Item", "Edit Item Price", "Edit Item Stock", "Back"]
		menu = basic_menu(select_menu_title, select_menu_items)
		index = menu.show()

		if index == 0:
			item_name = input("Enter item name: ")
			min_price = float(input("Enter minimum price: "))
			max_price = float(input("Enter maximum price: "))
			stock = int(input("Enter stock: "))

			item_types = get_item_types()
			if item_types:
				item_type_id = select_item(item_types, "Select an item type:")
				add_item(item_name, min_price, max_price, stock, shop_id, item_type_id)
			else:
				print(colored("No item types found.", color='red', attrs=['bold']))

		elif index == 1:
			if items:
				item_id = select_item(items, "Select item to remove:")
				if not item_id:
					break
				remove_item(item_id)
			else:
				print(colored("No items found.", color='red', attrs=['bold']))

		elif index == 2:
			if items:
				item_id = select_item(items, "Select item to edit price:")
				if not item_id:
					break
				min_price = float(input("Enter new minimum price: "))
				max_price = float(input("Enter new maximum price: "))
				edit_item_price(item_id, min_price, max_price)
			else:
				print(colored("No items found.", color='red', attrs=['bold']))

		elif index == 3:
			if items:
				item_id = select_item(items, "Select item to edit stock:")
				if not item_id:
					break
				stock = int(input("Enter new stock: "))
				edit_item_stock(item_id, stock)

		else:
			print(colored("No items found.", color='red', attrs=['bold']))
			break


def manage_item_types():
	while True:
		select_menu_title = "Select an option"
		select_menu_items = ["Add Item Type", "Remove Item Type", "Edit Item Type", "Back"]
		menu = TerminalMenu(select_menu_items, title=select_menu_title)
		index = menu.show()

		if index == 0:
			item_type_name = input(colored("Enter item type name: ", attrs=['bold']))
			size = input(colored("Enter item type size: ", attrs=['bold']))
			wealth_factor = int(input(colored("Enter item type wealth factor (1-10): ", attrs=['bold'])))
			min_amount = int(input(colored("Enter item type minimum amount: ", attrs=['bold'])))
			max_amount = int(input(colored("Enter item type maximum amount: ", attrs=['bold'])))

			conn = sqlite3.connect('mydatabase.sqlite')
			c = conn.cursor()

			c.execute("INSERT INTO item_types (name, size, wealth_factor, min_amount, max_amount) VALUES (?, ?, ?, ?, ?)",
					  (item_type_name, size, wealth_factor, min_amount, max_amount))

			conn.commit()
			conn.close()
		elif index == 1:
			conn = sqlite3.connect('mydatabase.sqlite')
			c = conn.cursor()

			c.execute("SELECT * FROM item_types")
			item_types = c.fetchall()

			conn.close()

			if item_types:
				print(colored("Select item type to remove:", attrs=['bold']))
				item_type_menu = TerminalMenu([item_type[1] for item_type in item_types])
				item_type_index = item_type_menu.show()
				item_type_id = item_types[item_type_index][0]

				conn = sqlite3.connect('mydatabase.sqlite')
				c = conn.cursor()

				c.execute("DELETE FROM item_types WHERE id=?", (item_type_id,))

				conn.commit()
				conn.close()
			else:
				print(colored("No item types found.", color='red', attrs=['bold']))
		elif index == 2:
			conn = sqlite3.connect('mydatabase.sqlite')
			c = conn.cursor()

			c.execute("SELECT * FROM item_types")
			item_types = c.fetchall()

			conn.close()

			if item_types:
				while True:
					print(colored("Select item type to edit:", attrs=['bold']))
					item_type_menu = TerminalMenu([item_type[1] for item_type in item_types])
					item_type_index = item_type_menu.show()
					item_type_id = item_types[item_type_index][0]

					item_type_name = input(colored("Enter new item type name (blank to skip): ", attrs=['bold']))
					size = input(colored("Enter new item type size (blank to skip): ", attrs=['bold']))
					wealth_factor = input(colored("Enter new item type wealth factor (1-10) (blank to skip): ", attrs=['bold']))
					min_amount = input(colored("Enter new item type minimum amount (blank to skip): ", attrs=['bold']))
					max_amount = input(colored("Enter new item type maximum amount (blank to skip): ", attrs=['bold']))

					conn = sqlite3.connect('mydatabase.sqlite')
					c = conn.cursor()

					update_query = "UPDATE item_types SET "
					update_params = []
					if item_type_name:
						update_query += "name=?, "
						update_params.append(item_type_name)
					if size:
						update_query += "size=?, "
						update_params.append(size)
					if wealth_factor:
						update_query += "wealth_factor=?, "
						update_params.append(wealth_factor)
					if min_amount:
						update_query += "min_amount=?, "
						update_params.append(min_amount)
					if max_amount:
						update_query += "max_amount=?, "
						update_params.append(max_amount)

					if not update_params:
						print(colored("No changes made.", color='yellow', attrs=['bold']))
						break

					update_query = update_query.rstrip(", ") + " WHERE id=?"
					update_params.append(item_type_id)

					c.execute(update_query, tuple(update_params))

					conn.commit()
					conn.close()

					print(colored("Item type updated successfully.", color='green', attrs=['bold']))

					choice = input(colored("Do you want to edit another item type? (y/n): ", attrs=['bold']))
					if choice.lower() != 'y':
						break
			else:
				print(colored("No item types found.", color='red', attrs=['bold']))
		elif index == 3:
			break