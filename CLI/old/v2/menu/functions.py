from database.database_operation import get_countries, get_cities_by_country, get_shops_by_city

from simple_term_menu import TerminalMenu
from termcolor import colored
from tabulate import tabulate

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

def select_country_menu():
    countries = get_countries()
    country_menu_items = [f"{country.name}" for country in countries]
    country_menu_items.append("Back")
    country_menu = basic_menu("Select a country", country_menu_items)
    country_choice = country_menu.show()

    if country_choice == len(country_menu_items) - 1:
        return None

    return countries[country_choice]


def select_city_menu(country_id):
    cities = get_cities_by_country(country_id)
    city_menu_items = [f"{city.name}" for city in cities]
    city_menu_items.append("Back")
    city_menu = basic_menu("Select a city", city_menu_items)
    city_choice = city_menu.show()

    if city_choice == len(city_menu_items) - 1:
        return None

    return cities[city_choice]


def select_shop_menu(city_id):
    shops = get_shops_by_city(city_id)
    shop_menu_items = [f"{shop.name}" for shop in shops]
    shop_menu_items.append("Back")
    shop_menu = basic_menu("Select a shop", shop_menu_items)
    shop_choice = shop_menu.show()

    if shop_choice == len(shop_menu_items) - 1:
        return None

    return shops[shop_choice]

def print_formatted_dataframe(df):
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

def print_colored_dataframe(df):
    headers = list(df.columns)
    rows = []
    for _, row in df.iterrows():
        row_values = [colored(str(value), "cyan") for value in row.values]
        rows.append(row_values)
    print(tabulate(rows, headers=headers, tablefmt='plain'))
    
def convert_currency_to_copper(currency):
    value, unit = currency.split(' ')
    value = float(value)
    unit = unit.lower()

    # Convert the currency to copper (cp)
    if unit == 'cp':
        return int(value)
    elif unit == 'sp':
        return int(value * 10)
    elif unit == 'ep':
        return int(value * 50)
    elif unit == 'gp':
        return int(value * 100)
    elif unit == 'pp':
        return int(value * 1000)
    else:
        print(f"Invalid currency unit: {unit}. Defaulting to 0 cp.")
        return 0


def convert_currency_to_copper(currency):
    currency = currency.strip().lower()
    if currency.endswith("cp"):
        return int(currency[:-2])
    elif currency.endswith("sp"):
        return int(currency[:-2]) * 10
    elif currency.endswith("gp"):
        return int(currency[:-2]) * 100
    elif currency.endswith("pp"):
        return int(currency[:-2]) * 1000
    else:
        print(colored(f"Invalid currency format: {currency}. Using default value (0 cp).", color='yellow'))
        return 0