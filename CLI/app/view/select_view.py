from termcolor import colored
from simple_term_menu import TerminalMenu

import os


def basic_menu(title, menu_entries, color='yellow'):
    menu_cursor = "> "
    menu_cursor_style = ("fg_yellow", "bold")
    menu_highlight_style = ("fg_blue", "bold")

    print(colored(title, color, attrs=['bold']))
    return TerminalMenu(menu_entries=menu_entries,
                        menu_cursor=menu_cursor,
                        menu_cursor_style=menu_cursor_style,
                        menu_highlight_style=menu_highlight_style)
    

def clear_terminal():
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def select_kingdom(session, kingdom_handler):
    kingdoms = kingdom_handler.select_all(session)
    if not kingdoms:
        print(colored("No kingdoms found.", 'yellow'))
        return None

    kingdom_menu = basic_menu("Select a Kingdom:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    return selected_kingdom

def select_city(session, city_handler, kingdom_id):
    cities = city_handler.select_by_kingdom(session, kingdom_id)
    if not cities:
        print(colored("No kingdoms found.", 'yellow'))
        return None

    city_menu = basic_menu("Select a City:", [city.name for city in cities])
    selected_city_index = city_menu.show()
    selected_city = cities[selected_city_index]

    return selected_city

def select_shop(session, shop_handler, city_id):
    shops = shop_handler.select_by_city(session, city_id)
    if not shops:
        print(colored("No shops found.", 'yellow'))
        return None
    shop_menu = basic_menu("Select a Shop:", [shop.name for shop in shops])
    selected_shop_index = shop_menu.show()
    selected_shop = shops[selected_shop_index]

    return selected_shop

def select_shops(session, city_handler, shop_handler, kingdom_handler):
    selected_shops = []

    # Select a kingdom
    selected_kingdom = select_kingdom(session, kingdom_handler)
    clear_terminal()
    if selected_kingdom is None:
        return

    # Select a city
    selected_city = select_city(session, city_handler, selected_kingdom.id)
    clear_terminal()
    if selected_city is None:
        return

    # List all available shops in the selected city
    available_shops = shop_handler.select_by_city(session, selected_city.id)

    while available_shops:
        shop_menu = basic_menu("Select a Shop to add to the export list:", [shop.name for shop in available_shops] + ["Done"])
        clear_terminal()
        selected_shop_index = shop_menu.show()

        if selected_shop_index == len(available_shops):  # User selected "Done"
            break

        selected_shop = available_shops[selected_shop_index]
        selected_shops.append(selected_shop)
        
        # Remove the selected shop from the available shops list
        available_shops.remove(selected_shop)
        print(colored(selected_shop.name, 'yellow'))

    if not selected_shops:
        print(colored("No shop selected.", 'yellow'))

    return selected_shops



def select_shop_type(session, shop_type_handler):
    shop_types = shop_type_handler.select_all(session)
    if not shop_types:
        print(colored("No shop types found.", 'yellow'))
        return None
    shop_type_menu = basic_menu("Select a Shop Type:", [shop_type.shop_type for shop_type in shop_types])
    selected_shop_type_index = shop_type_menu.show()
    selected_shop_type = shop_types[selected_shop_type_index]

    return selected_shop_type

def select_item_type(session, item_type_handler):
    item_types = item_type_handler.select_all(session)
    if not item_types:
        print(colored("No item types found.", 'yellow'))
        return None
    item_type_menu = basic_menu("Select an Item Type:", [f"{item_type.item_type} - {item_type.sub_type}" for item_type in item_types])
    selected_item_type_index = item_type_menu.show()
    selected_item_type = item_types[selected_item_type_index]

    return selected_item_type

def select_item(session, item_handler, shop_id):
    items = item_handler.select_by_shop(session, shop_id)
    if not items:
        print(colored("No items found.", 'yellow'))
        return None
    item_menu = basic_menu("Select an Item to Delete:", [item.name for item in items])
    selected_item_index = item_menu.show()
    selected_item = items[selected_item_index]

    return selected_item

def select_item_for_update(session, item_handler, shop_id):
    items = item_handler.select_by_shop(session, shop_id)
    if not items:
        print(colored("No items to update found.", 'yellow'))
        return None
    item_menu = basic_menu("Select an Item to Update:", [item.name for item in items])
    selected_item_index = item_menu.show()
    selected_item = items[selected_item_index]

    return selected_item