# view/shop_view.py
from controller.handle_kingdom import KingdomHandler
from controller.handle_city import CityHandler
from controller.handle_shop_type import ShopTypeHandler
from controller.handle_shop import ShopHandler
from controller.handle_item import ItemHandler
from controller.handle_item_type import ItemTypeHandler
from terminal_menu import create_menu
from termcolor import colored

def add_item_view(session):
    # Create handlers
    item_handler = ItemHandler()
    item_type_handler = ItemTypeHandler()
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_handler = ShopHandler()

    # Select a Kingdom
    kingdoms = kingdom_handler.select_all(session)
    kingdom_menu = create_menu("Select a Kingdom:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    # Select a City
    cities = city_handler.select_by_kingdom(session, selected_kingdom.id)
    city_menu = create_menu("Select a City:", [city.name for city in cities])
    selected_city_index = city_menu.show()
    selected_city = cities[selected_city_index]

    # Select a Shop
    shops = shop_handler.select_by_city(session, selected_city.id)
    shop_menu = create_menu("Select a Shop:", [shop.name for shop in shops])
    selected_shop_index = shop_menu.show()
    selected_shop = shops[selected_shop_index]
    
    # Enter Item Name
    item_name = input("Enter the item name: ")

    # Enter prices
    current_price = float(input("Enter the current price: "))
    min_price = float(input("Enter the minimum price: "))
    max_price = float(input("Enter the maximum price: "))

    # Enter amount
    current_amount = float(input("Enter the current amount: "))

    # Select Item Type
    item_types = item_type_handler.select_all(session)
    item_type_menu = create_menu("Select an Item Type:", [item_type.name for item_type in item_types])
    selected_item_type_index = item_type_menu.show()
    selected_item_type = item_types[selected_item_type_index]

    # Add the item
    item_handler.add(session, item_name, current_price, min_price, max_price, current_amount, selected_item_type.id, selected_shop.id)
    print("Item added successfully!")


def delete_item_view(session):
    # Create handler
    item_handler = ItemHandler()

    # Select an Item
    items = item_handler.select_all(session)
    item_menu = create_menu("Select an Item to Delete:", [item.name for item in items])
    selected_item_index = item_menu.show()
    selected_item = items[selected_item_index]

    # Confirm deletion
    confirmation_menu = create_menu("Are you sure you want to delete this item?", ["Yes", "No"])
    confirmation_index = confirmation_menu.show()

    if confirmation_index == 0:  # User selected "Yes"
        # Delete the item
        item_handler.delete(session, selected_item.id)
        print("Item deleted successfully!")
    else:
        print("Item deletion cancelled.")
        
        
def update_item_view(session):
    # Create handlers
    item_handler = ItemHandler()
    item_type_handler = ItemTypeHandler()
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_handler = ShopHandler()

    # Select a Kingdom
    kingdoms = kingdom_handler.select_all(session)
    kingdom_menu = create_menu("Select a Kingdom:", [kingdom.name for kingdom in kingdoms])
    selected_kingdom_index = kingdom_menu.show()
    selected_kingdom = kingdoms[selected_kingdom_index]

    # Select a City
    cities = city_handler.select_by_kingdom(session, selected_kingdom.id)
    city_menu = create_menu("Select a City:", [city.name for city in cities])
    selected_city_index = city_menu.show()
    selected_city = cities[selected_city_index]

    # Select a Shop
    shops = shop_handler.select_by_city(session, selected_city.id)
    shop_menu = create_menu("Select a Shop:", [shop.name for shop in shops])
    selected_shop_index = shop_menu.show()
    selected_shop = shops[selected_shop_index]

    # Select an Item
    items = item_handler.select_by_shop(session, selected_shop.id)
    item_menu = create_menu("Select an Item to Update:", [item.name for item in items])
    selected_item_index = item_menu.show()
    selected_item = items[selected_item_index]

    # Select an Item
    items = item_handler.select_all(session)
    item_menu = create_menu("Select an Item to Update:", [item.name for item in items])
    selected_item_index = item_menu.show()
    selected_item = items[selected_item_index]

    while True:
        # Select a property to update
        properties_menu = create_menu("Select a property to update or go back:", ["Name", "Current Price", "Minimum Price", "Maximum Price", "Current Amount", "Item Type", "Shop", "Go back"])
        selected_property_index = properties_menu.show()

        if selected_property_index == 0:  # Update Name
            new_item_name = input("Enter the new item name: ")
            item_handler.update(session, selected_item.id, name=new_item_name)
        elif selected_property_index == 1:  # Update Current Price
            new_current_price = float(input("Enter the new current price: "))
            item_handler.update(session, selected_item.id, current_price=new_current_price)
        elif selected_property_index == 2:  # Update Minimum Price
            new_min_price = float(input("Enter the new minimum price: "))
            item_handler.update(session, selected_item.id, min_price=new_min_price)
        elif selected_property_index == 3:  # Update Maximum Price
            new_max_price = float(input("Enter the new maximum price: "))
            item_handler.update(session, selected_item.id, max_price=new_max_price)
        elif selected_property_index == 4:  # Update Current Amount
            new_current_amount = float(input("Enter the new current amount: "))
            item_handler.update(session, selected_item.id, current_amount=new_current_amount)
        elif selected_property_index == 5:  # Update Item Type
            item_types = item_type_handler.select_all(session)
            item_type_menu = create_menu("Select a new Item Type:", [item_type.name for item_type in item_types])
            selected_item_type_index = item_type_menu.show()
            selected_item_type = item_types[selected_item_type_index]
            item_handler.update(session, selected_item.id, item_type_id=selected_item_type.id)
        elif selected_property_index == 6:  # Update Shop
            shops = shop_handler.select_all(session)
            shop_menu = create_menu("Select a new Shop:", [shop.name for shop in shops])
            selected_shop_index = shop_menu.show()
            selected_shop = shops[selected_shop_index]
            item_handler.update(session, selected_item.id, shop_id=selected_shop.id)
        else:  # Go back
            break

    print("Item updated successfully!")
        

def show_all_in_shop_view(session):
    # Create handlers
    shop_handler = ShopHandler()
    item_handler = ItemHandler()

    # Select a Shop
    shops = shop_handler.select_all(session)
    shop_menu = create_menu("Select a Shop:", [shop.name for shop in shops])
    selected_shop_index = shop_menu.show()
    selected_shop = shops[selected_shop_index]

    # Show all items in the selected shop
    items = item_handler.select_by_shop(session, selected_shop.id)
    for item in items:
        print(item)