from controller.handle_kingdom import KingdomHandler
from controller.handle_city import CityHandler
from controller.handle_shop import ShopHandler
from controller.handle_item_type import ItemTypeHandler
from controller.handle_item import ItemHandler
from model.currency_conversions import convert_to_highest_currency
from view.select_view import select_shops, clear_terminal

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import six
from termcolor import colored
import pandas as pd
import csv
import os

def manage_export_csv(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_handler = ShopHandler()
    item_type_handler = ItemTypeHandler()
    item_handler = ItemHandler()
    # Select one or multiple shops
    selected_shops = select_shops(session, city_handler, shop_handler, kingdom_handler)
    clear_terminal()
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

            item_type = item_type_handler.select(session, item.item_type_id)

            data.append({
                'name': item.name,
                'current_price': f"{highest_currency_price} {currency_marker}",
                'current_amount': int(item.current_amount),
                'item_type;sub_type': f"{item_type.item_type};{item_type.sub_type}",
            })

        # Write data to CSV
        counter = 1
        filename = f"data/export/{shop.name}_items_v{counter}.csv"
        while os.path.exists(filename):
            enumerated_filename = f"data/export/{shop.name}_items_v{counter}.csv"
            filename = enumerated_filename
            counter += 1
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'current_price', 'current_amount', 'item_type;sub_type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)

        print(colored(f"Items from shop {shop.name} exported successfully!", "green"))

def manage_export_pdf(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_handler = ShopHandler()
    item_type_handler = ItemTypeHandler()
    item_handler = ItemHandler()
    # Select one or multiple shops
    selected_shops = select_shops(session, city_handler, shop_handler, kingdom_handler)
    clear_terminal()
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

            item_type = item_type_handler.select(session, item.item_type_id)

            data.append({
                'name': item.name,
                'current_price': f"{highest_currency_price} {currency_marker}",
                'current_amount': int(item.current_amount),
            })


        # Convert the data to a DataFrame
        df = pd.DataFrame(data)

        # Rename the columns
        df = df.rename(columns={
            "name": "Item Name",
            "current_price": "Price",
            "current_amount": "Stock",
        })

        # Create a new PDF
        counter = 1
        filename_pdf = f"data/export/{shop.name}_itemListv{counter}.pdf"
        while os.path.exists(filename_pdf):
            filename_pdf = f"data/export/{shop.name}_itemList_v{counter}.pdf"
            counter += 1
        
        render_mpl_table(df, header_columns=0, col_width=2.0)

        plt.savefig(filename_pdf)

        print(colored(f"Items from shop {shop.name} exported successfully to PDF!", "green"))
        
import matplotlib.pyplot as plt
import six

def render_mpl_table(data, col_width=6, row_height=0.625, font_size=14,
                     header_color='#f7cb4d', row_colors=['#fef8e3', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)


    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        cell.get_text().set_wrap(True)
        if k[0] == 0:
            cell.set_text_props(weight='bold', color='black', horizontalalignment='center')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors)])
            cell._text.set_horizontalalignment('left')

    return ax