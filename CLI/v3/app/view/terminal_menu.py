from ..controller.handle import handle_city, handle_item, handle_item_type, handle_kingdom, handle_shop, handle_shop_type, handle_import_export, handle_show_data
from ..model.kingdom import Kingdom
from ..model.city import City
from ..model.shop import Shop
from ..model.item import Item
from ..model.item_type import ItemType
from ..model.shop_type import ShopType

from simple_term_menu import TerminalMenu
import os
from termcolor import colored
from time import sleep

def create_menu(title, menu_entries, color='yellow'):
    menu_cursor = "> "
    menu_cursor_style = ("fg_yellow", "bold")
    menu_highlight_style = ("fg_blue", "bold")

    print(colored(title, color, attrs=['bold']))
    return TerminalMenu(menu_entries=menu_entries,
                        menu_cursor=menu_cursor,
                        menu_cursor_style=menu_cursor_style,
                        menu_highlight_style=menu_highlight_style)

def clear_terminal():
    _ = os.system("clear")

def get_entities(entity, session, parent_entity=None):
    if entity == 'Kingdom':
        kingdoms = session.query(Kingdom).all()
        if not kingdoms:
            print(colored("No Kingdoms found to select from.", 'red'))
            return []
        return [kingdom.name for kingdom in kingdoms]
    elif entity == 'Cities':
        if parent_entity and isinstance(parent_entity, Kingdom):
            cities = parent_entity.cities
            if cities:
                return [city.name for city in cities]
        print(colored("No Cities found to select from.", 'red'))
        return []
    elif entity == 'Shops':
        if parent_entity and isinstance(parent_entity, City):
            shops = parent_entity.shops
            if shops:
                return [shop.name for shop in shops]
        print(colored("No Shops found to select from.", 'red'))
        return []
    elif entity == 'Items':
        if parent_entity and isinstance(parent_entity, Shop):
            items = parent_entity.items
            if items:
                return [item.name for item in items]
        print(colored("No Items found to select from.", 'red'))
        return []
    elif entity == 'Item Type':
        item_types = session.query(ItemType).all()
        if not item_types:
            print(colored("No Item Types found to select from.", 'red'))
            return []
        return [item_type.name for item_type in item_types]
    elif entity == 'Shop Type':
        shop_types = session.query(ShopType).all()
        if not shop_types:
            print(colored("No Shop Types found to select from.", 'red'))
            return []
        return [shop_type.name for shop_type in shop_types]
    else:
        print(colored(f"Invalid entity: {entity}.", 'red'))
        return []


def manage_entity(session, entity, dependencies=[], parent_entity=None):
    entity_handlers = {
        "Kingdom": handle_kingdom.handle_kingdom,
        "City": handle_city.handle_city,
        "Shop": handle_shop.handle_shop,
        "Item": handle_item.handle_item,
        "Item Type": handle_item_type.handle_item_type,
        "Shop Type": handle_shop_type.handle_shop_type
    }

    while True:
        context = {}
        for dependency in dependencies:
            selected = choose_entity(session, dependency, context, parent_entity)
            if selected is None:
                break  # Go back was selected, break out of the loop
            else:
                context[dependency] = selected

        if len(context) < len(dependencies):
            break  # Go back was selected in one of the dependencies, so don't display the entity menu

        parent_entity = None
        if context:  # If there is any entity in the context, it's the parent entity
            parent_entity_key = list(context.keys())[-1]  # Get the last entity in the context
            parent_entity = context[parent_entity_key]

        menu_entries = ["Add", "Update", "Delete", "Select", "Go back"]
        menu = create_menu(f"Manage {entity}", menu_entries)
        menu_choice = menu.show()
        clear_terminal()

        if menu_choice == len(menu_entries) - 1:  # "Go back" selected
            break
        else:
            action = menu_entries[menu_choice]
            entity_handlers[entity](action, session, context, entity, parent_entity)


def choose_entity(session, entity, context, parent_entity=None):
    menu_entries = get_entities(entity, session, parent_entity)

    if not menu_entries:
        print(colored(f"No {entity} to choose from the database.", 'red'))
        sleep(1)
        clear_terminal()
        return
    menu_entries += ['Go back']
    menu = create_menu(f"Select {entity}", menu_entries)
    menu_choice = menu.show()
    clear_terminal()

    if menu_choice != len(menu_entries) - 1:  # If "Go back" was not chosen
        selected_entity_name = menu_entries[menu_choice]
        if entity == 'Kingdom':
            selected_entity = session.query(Kingdom).filter(Kingdom.name == selected_entity_name).first()
        elif entity == 'City':
            selected_entity = session.query(City).filter(City.name == selected_entity_name).first()
        elif entity == 'Shop':
            selected_entity = session.query(Shop).filter(Shop.name == selected_entity_name).first()
        elif entity == 'Item':
            selected_entity = session.query(Item).filter(Item.name == selected_entity_name).first()
        elif entity == 'ItemType':
            selected_entity = session.query(ItemType).filter(ItemType.name == selected_entity_name).first()
        elif entity == 'ShopType':
            selected_entity = session.query(ShopType).filter(ShopType.name == selected_entity_name).first()

        return selected_entity  # Return the selected entity object, not just the name
    else:
        return None


def handle_manage_operations(session):
    while True:
        main_menu_entries = ["Kingdom", "City", "Shop", "Item", "Item Type", "Shop Type", "Go back"]
        main_menu = create_menu("Manage World", main_menu_entries)
        main_menu_choice = main_menu.show()
        clear_terminal()

        if main_menu_choice == 0:  # "Manage Kingdom"
            manage_entity(session, 'Kingdom')

        elif main_menu_choice == 1:  # "Manage City"
            manage_entity(session, 'City', ['Kingdom'], parent_entity=Kingdom)

        elif main_menu_choice == 2:  # "Manage Shop"
            manage_entity(session, 'Shop', ['Kingdom', 'City'], parent_entity=City)

        elif main_menu_choice == 3:  # "Manage Item"
            manage_entity(session, 'Item', ['Kingdom', 'City', 'Shop'], parent_entity=Shop)

        elif main_menu_choice == 4:  # "Manage Item Type"
            manage_entity(session, 'Item Type')
            
        elif main_menu_choice == 5:  # "Manage Shop Type"
            manage_entity(session, 'Shop Type')

        elif main_menu_choice == 6:  # "Exit"
            break

def display_menu(session):
    clear_terminal()
    while True:
        menu_entries = ["Manage World", "Show Data", "Import/Export", "Exit"]
        menu = create_menu("Main Menu", menu_entries)
        menu_choice = menu.show()
        clear_terminal()

        if menu_choice == 0:  # "Management Operations" selected
            handle_manage_operations(session)
        elif menu_choice == 1:  # "Show Data" selected
            handle_show_data.handle_show_data()
        elif menu_choice == 2:  # "Import/Export" selected
            handle_import_export.handle_import_export()
        elif menu_choice == 3:  # "Exit" selected
            break