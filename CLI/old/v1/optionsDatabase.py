import sqlite3
import csv
from termcolor import colored

def save_data(timestamp, value):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute('INSERT INTO currency VALUES (?, ?)', (timestamp, value))

    conn.commit()
    conn.close()


def add_country(name):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO countries (name) VALUES (?)", (name,))

    conn.commit()
    conn.close()


def remove_country(country_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("DELETE FROM countries WHERE id=?", (country_id,))

    conn.commit()
    conn.close()


def add_city(name, population, wealth_factor, country_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO cities (name, population, wealth_factor, country_id) VALUES (?, ?, ?, ?)",
              (name, population, wealth_factor, country_id))

    conn.commit()
    conn.close()


def remove_city(city_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("DELETE FROM cities WHERE id=?", (city_id,))

    conn.commit()
    conn.close()


def add_shop(name, city_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO shops (name, city_id) VALUES (?, ?)", (name, city_id))

    conn.commit()
    conn.close()


def remove_shop(shop_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("DELETE FROM shops WHERE id=?", (shop_id,))

    conn.commit()
    conn.close()


def add_item(name, min_price, max_price, shop_id, item_type_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO items (name, min_price, max_price, shop_id, item_type_id) VALUES (?, ?, ?, ?, ?)",
              (name, min_price, max_price, shop_id, item_type_id))

    conn.commit()
    conn.close()


def remove_item(item_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("DELETE FROM items WHERE id=?", (item_id,))

    conn.commit()
    conn.close()


def edit_item_price(item_id, min_price, max_price):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("UPDATE items SET min_price=?, max_price=? WHERE id=?", (min_price, max_price, item_id))

    conn.commit()
    conn.close()


def edit_item_stock(item_id, stock):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("UPDATE items SET stock=? WHERE id=?", (stock, item_id))

    conn.commit()
    conn.close()

def add_item_type(item_type_name, size, wealth_factor, min_amount, max_amount):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO item_types (name, wealth_factor, min_amount, max_amount) VALUES (?, ?, ?, ?)",
              (item_type_name, wealth_factor, min_amount, max_amount))

    conn.commit()
    item_type_id = c.lastrowid
    conn.close()

    print(colored("Item type added successfully.", color='green', attrs=['bold']))
    return item_type_id

def get_countries():
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM countries")
    countries = c.fetchall()

    conn.close()

    return countries

def get_cities(country_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM cities WHERE country_id=?", (country_id,))
    cities = c.fetchall()

    conn.close()

    return cities


def get_shops(city_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM shops WHERE city_id=?", (city_id,))
    shops = c.fetchall()

    conn.close()

    return shops

def get_shop_name(shop_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    # Execute the query to retrieve the shop name
    c.execute("SELECT name FROM shops WHERE id=?", (shop_id,))
    result = c.fetchone()

    if result:
        shop_name = result[0]
        return shop_name

    return None

def get_items(shop_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    # Execute the query to retrieve items in the shop
    c.execute("SELECT id, name, item_type_id, min_price, max_price FROM items WHERE shop_id=?", (shop_id,))
    items = c.fetchall()

    return items


def get_item_types():
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM item_types")
    item_types = c.fetchall()

    conn.close()

    return item_types

def get_item_type_name(item_type_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    # Execute the query to retrieve the item type name
    c.execute("SELECT name FROM item_types WHERE id=?", (item_type_id,))
    result = c.fetchone()

    if result:
        item_type_name = result[0]
        return item_type_name

    return None

def get_item_type_id(item_type_name):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("SELECT id FROM item_types WHERE name=?", (item_type_name,))
    result = c.fetchone()

    conn.close()

    return result[0] if result else None

def show_countries():
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM countries")
    countries = c.fetchall()

    print("\n--- Countries ---")
    for country in countries:
        print(f"ID: {country[0]}, Name: {country[1]}, Wealth Factor: {country[2]}")

    conn.close()


def show_cities(country_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM cities WHERE country_id=?", (country_id,))
    cities = c.fetchall()

    print("\n--- Cities ---")
    for city in cities:
        print(f"ID: {city[0]}, Name: {city[1]}, Population: {city[2]}, Wealth Factor: {city[3]}")

    conn.close()


def show_shops(city_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM shops WHERE city_id=?", (city_id,))
    shops = c.fetchall()

    print("\n--- Shops ---")
    for shop in shops:
        print(f"ID: {shop[0]}, Name: {shop[1]}")

    conn.close()


def show_items(shop_id):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("SELECT * FROM items WHERE shop_id=?", (shop_id,))
    items = c.fetchall()

    print("\n--- Items ---")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}, Min Price: {item[2]}, Max Price: {item[3]}")

    conn.close()

def update_city_name(city_id, new_name):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("UPDATE cities SET name=? WHERE id=?", (new_name, city_id))

    conn.commit()
    conn.close()


def update_city_population(city_id, new_population):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("UPDATE cities SET population=? WHERE id=?", (new_population, city_id))

    conn.commit()
    conn.close()


def update_city_wealth_factor(city_id, new_wealth_factor):
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute("UPDATE cities SET wealth_factor=? WHERE id=?", (new_wealth_factor, city_id))

    conn.commit()
    conn.close()