from .database_setup import session, Country, City, Shop, ItemType, Item
from termcolor import colored


def get_countries():
    return session.query(Country).all()


def get_cities():
    return session.query(City).all()

def get_cities_by_country(country_id):
    cities = session.query(City).filter(City.country_id == country_id).all()
    return cities

def get_shops():
    return session.query(Shop).all()

def get_shops_by_city(city_id):
    shops = session.query(Shop).filter(Shop.city_id == city_id).all()
    return shops

def get_item_types():
    return session.query(ItemType).all()

def get_item_type_by_name(item_type_name, item_type_subtype):
    return session.query(ItemType).filter_by(type=item_type_name, sub_type=item_type_subtype).first()

def get_item_type_by_id(item_type_id):
    item_type = session.query(ItemType).filter_by(id=item_type_id).first()
    return item_type

def get_items(shop_id):
    items = session.query(Item).filter_by(shop_id=shop_id).all()
    return items


def add_country(name):
    country = Country(name=name)
    session.add(country)
    session.commit()


def add_city(name, population, wealth_indicator, country_id):
    city = City(name=name, population=population, wealth_indicator=wealth_indicator, country_id=country_id)
    session.add(city)
    session.commit()


def add_shop(name, city_id):
    shop = Shop(name=name, city_id=city_id)
    session.add(shop)
    session.commit()
    return shop 


def add_item_type(name, subtype, min_amount, max_amount, wealth_factor):
    item_type = session.query(ItemType).filter_by(name=name, subtype=subtype).first()
    if item_type:
        return item_type

    try:
        item_type = ItemType(name=name, subtype=subtype, min_amount=min_amount, max_amount=max_amount,
                             wealth_factor=wealth_factor)
        session.add(item_type)
        session.commit()
        return item_type
    except Exception as e:
        session.rollback()
        print(colored(f"Failed to create item type: {str(e)}", color='red'))
        return None


def add_item(name, current_price, min_price, max_price, current_amount, item_type_id, shop_id):
    try:
        item = Item(
            name=name,
            current_price=current_price,
            min_price=min_price,
            max_price=max_price,
            current_amount=current_amount,
            item_type_id=item_type_id,
            shop_id=shop_id
        )
        session.add(item)
        session.commit()
        return True, None
    except Exception as e:
        session.rollback()
        error_message = str(e)
        return False, error_message

def remove_country(country_id):
    country = session.query(Country).filter_by(id=country_id).first()
    if country:
        session.delete(country)
        session.commit()


def remove_city(city_id):
    city = session.query(City).filter_by(id=city_id).first()
    if city:
        session.delete(city)
        session.commit()


def remove_shop(shop_id):
    shop = session.query(Shop).filter_by(id=shop_id).first()
    if shop:
        session.delete(shop)
        session.commit()


def remove_item_type(item_type_id):
    item_type = session.query(ItemType).filter_by(id=item_type_id).first()
    if item_type:
        session.delete(item_type)
        session.commit()


def remove_item(item_id):
    item = session.query(Item).filter_by(id=item_id).first()
    if item:
        session.delete(item)
        session.commit()


def edit_country(country_id, name):
    country = session.query(Country).filter_by(id=country_id).first()
    if country:
        country.name = name
        session.commit()


def edit_city(city_id, name, population, wealth_indicator, country_id):
    city = session.query(City).filter_by(id=city_id).first()
    if city:
        city.name = name
        city.population = population
        city.wealth_indicator = wealth_indicator
        city.country_id = country_id
        session.commit()


def edit_shop(shop_id, name, city_id):
    shop = session.query(Shop).filter_by(id=shop_id).first()
    if shop:
        shop.name = name
        shop.city_id = city_id
        session.commit()


def edit_item_type(item_type_id, type, sub_type, min_amount, max_amount, wealth_indicator):
    item_type = session.query(ItemType).filter_by(id=item_type_id).first()
    if item_type:
        item_type.type = type
        item_type.sub_type = sub_type
        item_type.min_amount = min_amount
        item_type.max_amount = max_amount
        item_type.wealth_indicator = wealth_indicator
        session.commit()


def edit_item(item_id, name, current_price, min_price, max_price, current_amount, item_type_id, shop_id):
    item = session.query(Item).filter_by(id=item_id).first()
    if item:
        item.name = name
        item.current_price = current_price
        item.min_price = min_price
        item.max_price = max_price
        item.current_amount = current_amount
        item.item_type_id = item_type_id
        item.shop_id = shop_id
        session.commit()
