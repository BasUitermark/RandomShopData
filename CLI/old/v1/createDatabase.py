import os
import sqlite3

def create_database():
    create_table_countries()
    create_table_cities()
    create_table_shops()
    create_table_item_types()
    create_table_items()

def create_table_countries():
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')

    conn.commit()
    conn.close()


def create_table_cities():
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            population INTEGER,
            wealth_factor INTEGER,
            country_id INTEGER,
            FOREIGN KEY (country_id) REFERENCES countries (id)
        )
    ''')

    conn.commit()
    conn.close()


def create_table_shops():
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS shops (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            city_id INTEGER,
            FOREIGN KEY (city_id) REFERENCES cities (id)
        )
    ''')

    conn.commit()
    conn.close()


def create_table_items():
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            min_price REAL,
            max_price REAL,
            shop_id INTEGER,
            item_type_id INTEGER,
            FOREIGN KEY (shop_id) REFERENCES shops (id),
            FOREIGN KEY (item_type_id) REFERENCES item_types (id)
        )
    ''')

    conn.commit()
    conn.close()


def create_table_item_types():
    conn = sqlite3.connect('mydatabase.sqlite')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS item_types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            wealth_factor INTEGER,
            min_amount INTEGER,
            max_amount INTEGER
        )
    ''')

    conn.commit()
    conn.close()