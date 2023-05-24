import csv
from termcolor import colored
from controller.handle_kingdom import KingdomHandler
from controller.handle_city import CityHandler
from controller.handle_shop import ShopHandler
from controller.handle_item import ItemHandler
from model.currency_conversions import convert_to_highest_currency
from view.select_view import select_shops

def manage_export(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_handler = ShopHandler()
    item_handler = ItemHandler()
    # Select one or multiple shops
    selected_shops = select_shops(session, city_handler, shop_handler, kingdom_handler)
    if not selected_shops:
        return

    for shop in selected_shops:
        # Fetch items from the selected shop
        items = item_handler.select_by_shop(session, shop.id)

        # Prepare data for CSV
        data = []
        for item in items:
            # Convert price back to highest currency and add marker
            highest_currency_price, currency_marker = convert_to_highest_currency(item.current_price)

            data.append({
                'name': item.name,
                'current_price': f"{highest_currency_price} {currency_marker}",
                'current_amount': item.current_amount,
                'item_type;sub_type': f"{item.item_type.name};{item.item_type.sub_type}",
            })

        # Write data to CSV
        filename = f"data/export/{shop.name}_items.csv"
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'current_price', 'current_amount', 'item_type;sub_type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)

        print(colored(f"Items from shop {shop.name} exported successfully!", "green"))
