# view/shop_view.py
from .select_view import *
from controller.handle_kingdom import KingdomHandler
from controller.handle_city import CityHandler
from controller.handle_shop import ShopHandler
from controller.handle_item import ItemHandler
from controller.handle_item_type import ItemTypeHandler
from .select_view import basic_menu, clear_terminal
from termcolor import colored


def manage_item(session):
    global breadcrumbs
    while True:
        manage_menu_entries = ["Add Item", "Update Item", "Delete Item", "Show Items", "Go back"]
        manage_menu = basic_menu("Manage Item", manage_menu_entries)
        manage_menu_choice = manage_menu.show()
        clear_terminal()

        if manage_menu_choice == 0:  # "Add Item"
            breadcrumbs.append("Add Item")
            add_item_view(session)
            breadcrumbs = breadcrumbs[:-1]

        elif manage_menu_choice == 1:  # "Update Item"
            breadcrumbs.append("Update Item")
            update_item_view(session)
            breadcrumbs = breadcrumbs[:-1]

        elif manage_menu_choice == 2:  # "Delete Item"
            breadcrumbs.append("Delete Item")
            delete_item_view(session)
            breadcrumbs = breadcrumbs[:-1]

        elif manage_menu_choice == 3:  # "Show Items"
            breadcrumbs.append("Show Items")
            show_all_in_shop_view(session)
            breadcrumbs = breadcrumbs[:-1]

        elif manage_menu_choice == 4:  # "Go back"
            break


def add_item_view(session):
    # Create handlers
    item_handler = ItemHandler()
    item_type_handler = ItemTypeHandler()
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

    # Select a Shop
    selected_shop = select_shop(session, shop_handler, selected_city.id)
    if selected_shop is None:
        return

    # Enter Item Name
    item_name = input(colored("Enter the item name: ", attrs=['bold']))

    # Enter prices
    current_price = float(input(colored("Enter the current price: ", attrs=['bold'])))
    min_price = float(input(colored("Enter the minimum price: ", attrs=['bold'])))
    max_price = float(input(colored("Enter the maximum price: ", attrs=['bold'])))

    # Enter amount
    current_amount = float(input(colored("Enter the current amount: ", attrs=['bold'])))

    # Select Item Type
    selected_item_type = select_item_type(session, item_type_handler)

    # Add the item
    item_handler.add(session, item_name, current_price, min_price, max_price, current_amount, selected_item_type.id, selected_shop.id)
    print(colored("Item added successfully!",'green'))


def delete_item_view(session):
    # Create handler
    item_handler = ItemHandler()
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

    # Select a Shop
    selected_shop = select_shop(session, shop_handler, selected_city.id)
    if selected_shop is None:
        return

    # Select an Item
    selected_item = select_item(session, item_handler, selected_shop.id)
    if selected_item is None:
        return

    # Confirm deletion
    confirmation_menu = basic_menu("Are you sure you want to delete this item?", ["Yes", "No"])
    confirmation_index = confirmation_menu.show()

    if confirmation_index == 0:  # User selected "Yes"
        # Delete the item
        item_handler.delete(session, selected_item.id)
        print(colored("Item deleted successfully!", 'green'))
    else:
        print(colored("Item deletion cancelled.", 'yellow'))
        
        
def update_item_view(session):
    # Create handlers
    item_handler = ItemHandler()
    item_type_handler = ItemTypeHandler()
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

    # Select a Shop
    selected_shop = select_shop(session, shop_handler, selected_city.id)
    if selected_shop is None:
        return

    # Select an Item
    selected_item = select_item(session, item_handler, selected_shop.id)
    if selected_item is None:
        return

    while True:
        # Select a property to update
        properties_menu = basic_menu("Select a property to update or go back:", ["Name", "Current Price", "Minimum Price", "Maximum Price", "Current Amount", "Item Type", "Go back"])
        selected_property_index = properties_menu.show()

        if selected_property_index == 0:  # Update Name
            new_item_name = input(colored("Enter the new item name: ", attrs=['bold']))
            item_handler.update(session, selected_item.id, name=new_item_name)
            
        elif selected_property_index == 1:  # Update Current Price
            new_current_price = float(input(colored("Enter the new current price: ", attrs=['bold'])))
            item_handler.update(session, selected_item.id, current_price=new_current_price)
            
        elif selected_property_index == 2:  # Update Minimum Price
            new_min_price = float(input(colored("Enter the new minimum price: ", attrs=['bold'])))
            item_handler.update(session, selected_item.id, min_price=new_min_price)
            
        elif selected_property_index == 3:  # Update Maximum Price
            new_max_price = float(input(colored("Enter the new maximum price: ", attrs=['bold'])))
            item_handler.update(session, selected_item.id, max_price=new_max_price)
            
        elif selected_property_index == 4:  # Update Current Amount
            new_current_amount = float(input(colored("Enter the new current amount: ", attrs=['bold'])))
            item_handler.update(session, selected_item.id, current_amount=new_current_amount)
            
        elif selected_property_index == 5:  # Update Item Type
            selected_item_type = select_item_type(session, item_type_handler)
            item_handler.update(session, selected_item.id, item_type_id=selected_item_type.id)
            
        else:  # Go back
            break

    print(colored("Item updated successfully!", 'green'))
        

def show_all_in_shop_view(session):
    # Create handlers
    shop_handler = ShopHandler()
    item_handler = ItemHandler()
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

    # Show all items in the selected shop
    items = item_handler.select_by_shop(session, selected_shop.id)
    if items is None:
        return

    for item in items:
        print(item)