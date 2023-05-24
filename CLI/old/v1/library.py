from simple_term_menu import TerminalMenu

DATABASE_NAME = 'mydatabase.sqlite'

def basic_menu(title, menu_entries):
    menu_cursor = "> "
    menu_cursor_style = ("fg_yellow", "bold")
    menu_highlight_style = ("fg_blue", "bold")

    menu = TerminalMenu(menu_entries=menu_entries,
						title=title,
						menu_cursor=menu_cursor,
						menu_cursor_style=menu_cursor_style,
						menu_highlight_style=menu_highlight_style
    )
    return menu

def select_country(countries):
	country_menu_title = "Select Country"
	country_menu_items = [country[1] for country in countries]
	country_menu_items.append("Back")  # Add the "Back" option
	country_menu = basic_menu(country_menu_title, country_menu_items)
	country_index = country_menu.show()
	if country_index == len(countries):  # If "Back" option is chosen
		return None  # Return None to indicate going back
	country_id = countries[country_index][0]
	return country_id


def select_city(cities):
	city_menu_title = "Select a city:"
	city_menu_items = [city[1] for city in cities]
	city_menu_items.append("Back")  # Add the "Back" option
	city_menu = basic_menu(city_menu_title, city_menu_items)
	city_index = city_menu.show()
	if city_index == len(cities):  # If "Back" option is chosen
		return None  # Return None to indicate going back
	city_id = cities[city_index][0]
	return city_id


def select_shop(shops):
	shop_menu_title = "Select a shop:"
	shop_menu_items = [shop[1] for shop in shops]
	shop_menu_items.append("Back")  # Add the "Back" option
	shop_menu = basic_menu(shop_menu_title, shop_menu_items)
	shop_index = shop_menu.show()
	if shop_index == len(shops):  # If "Back" option is chosen
		return None  # Return None to indicate going back
	shop_id = shops[shop_index][0]
	return shop_id


def select_item(items):
	item_menu_title = "Select a item:"
	item_menu_items = [item[1] for item in items]
	item_menu_items.append("Back")  # Add the "Back" option
	item_menu = basic_menu(item_menu_title, item_menu_items)
	item_index = item_menu.show()
	if item_index == len(items):  # If "Back" option is chosen
		return None  # Return None to indicate going back
	item_id = items[item_index][0]
	return item_id

def convert_currency_to_copper(price):
    conversion_rates = {
        'pp': 10 * 10 * 10,  # Platinum to Gold to Silver to Copper
        'gp': 10 * 10,  # Gold to Silver to Copper
        'sp': 10,  # Silver to Copper
        'cp': 1  # Copper
    }

    price_parts = price.strip().split(' ')
    amount = int(price_parts[0])
    currency = price_parts[1]

    if currency not in conversion_rates:
        raise ValueError(f"Invalid currency: {currency}")

    copper_value = amount * conversion_rates[currency]
    return copper_value

def convert_copper_to_currency(copper_value):
    conversion_rates = {
        'pp': 10 * 10 * 10,  # Platinum to Gold to Silver to Copper
        'gp': 10 * 10,  # Gold to Silver to Copper
        'sp': 10,  # Silver to Copper
        'cp': 1  # Copper
    }

    conversion_order = ['pp', 'gp', 'sp', 'cp']
    result = ''

    for currency in conversion_order:
        conversion_rate = conversion_rates[currency]
        amount = copper_value // conversion_rate

        if amount > 0:
            result += f"{amount} {currency} "

        copper_value %= conversion_rate

    return result.strip()