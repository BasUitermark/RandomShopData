import pandas as pd
from .functions import create_menu, select_country_menu, select_city_menu, select_shop_menu, print_colored_dataframe, print_formatted_dataframe
from database.database_operation import get_countries, get_cities, get_shops, get_items, get_item_types, get_item_type_by_id

def show_data():
    while True:
        data_menu_title = "Show Data"
        data_menu_items = ["Show All Countries", "Show Cities of a Country", "Show Shops of a City",
                           "Show Items of a Shop", "Show Item Types", "Back"]
        data_menu = create_menu(data_menu_title, data_menu_items)
        data_choice = data_menu.show()

        if data_choice == 0:
            show_all_countries()

        elif data_choice == 1:
            show_cities_of_country()

        elif data_choice == 2:
            show_shops_of_city()

        elif data_choice == 3:
            show_items_of_shop()
            
        elif data_choice == 4:
            show_item_types()

        elif data_choice == 5:
            break

def show_all_countries():
    countries = get_countries()
    if not countries:
        print("No countries available.")
        return

    df = pd.DataFrame([(country.id, country.name) for country in countries], columns=["ID", "Name"])
    print_colored_dataframe(df)

def show_cities_of_country():
    country = select_country_menu()
    if not country:
        return

    cities = get_cities(country.id)
    if not cities:
        print("No cities available for the selected country.")
        return

    df = pd.DataFrame([(city.id, city.name, city.population, city.wealth_indicator) for city in cities],
                      columns=["ID", "Name", "Population", "Wealth Indicator"])
    print_colored_dataframe(df)

def show_shops_of_city():
    country = select_country_menu()
    if not country:
        return

    city = select_city_menu(country.id)
    if not city:
        return

    shops = get_shops(city.id)
    if not shops:
        print("No shops available for the selected city.")
        return

    df = pd.DataFrame([(shop.id, shop.name, len(shop.items)) for shop in shops],
                      columns=["ID", "Name", "Number of Items"])
    print_colored_dataframe(df)

def show_items_of_shop():
    country = select_country_menu()
    if not country:
        return

    city = select_city_menu(country.id)
    if not city:
        return

    shop = select_shop_menu(city.id)
    if not shop:
        return

    items = get_items(shop.id)
    if not items:
        print("No items available for the selected shop.")
        return

    data = []
    for item in items:
        item_type = get_item_type_by_id(item.item_type_id)
        data.append(
            (item.id, item.name, item.current_price, item.min_price, item.max_price, item.current_amount,
             item_type.type, item_type.sub_type)
        )

    df = pd.DataFrame(data, columns=["ID", "Item Name", "Current Price", "Min Price", "Max Price", "Current Amount",
                                     "Item Type", "Item Sub-Type"])
    print_colored_dataframe(df)
    
def show_item_types():
    item_types = get_item_types()
    if not item_types:
        print("No item types available.")
        return

    df = pd.DataFrame([(item_type.id, item_type.type, item_type.sub_type, item_type.min_amount, item_type.max_amount,
                        item_type.wealth_indicator) for item_type in item_types],
                      columns=["ID", "Item Type", "Item Sub-Type", "Min Amount", "Max Amount", "Wealth Indicator"])
    print_colored_dataframe(df)