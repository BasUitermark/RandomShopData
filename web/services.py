# services.py
from models import db, Country, City, Shop, ItemType, Item

def add_country(name):
    new_country = Country(name=name)
    db.session.add(new_country)
    db.session.commit()
    return new_country.id

def remove_country(id):
    country = Country.query.get(id)
    if country:
        db.session.delete(country)
        db.session.commit()

def update_country(id, name):
    country = Country.query.get(id)
    if country:
        country.name = name
        db.session.commit()

def add_city(name, population, wealth_indicator, country_id):
    new_city = City(name=name, population=population, wealth_indicator=wealth_indicator, country_id=country_id)
    db.session.add(new_city)
    db.session.commit()
    return new_city.id

def remove_city(id):
    city = City.query.get(id)
    if city:
        db.session.delete(city)
        db.session.commit()

def update_city(id, name, population, wealth_indicator, country_id):
    city = City.query.get(id)
    if city:
        city.name = name
        city.population = population
        city.wealth_indicator = wealth_indicator
        city.country_id = country_id
        db.session.commit()

def add_shop(name, city_id):
    new_shop = Shop(name=name, city_id=city_id)
    db.session.add(new_shop)
    db.session.commit()
    return new_shop.id

def remove_shop(id):
    shop = Shop.query.get(id)
    if shop:
        db.session.delete(shop)
        db.session.commit()

def update_shop(id, name, city_id):
    shop = Shop.query.get(id)
    if shop:
        shop.name = name
        shop.city_id = city_id
        db.session.commit()

def add_item_type(type, sub_type, min_amount, max_amount, wealth_indicator):
    new_item_type = ItemType(type=type, sub_type=sub_type, min_amount=min_amount, max_amount=max_amount, wealth_indicator=wealth_indicator)
    db.session.add(new_item_type)
    db.session.commit()
    return new_item_type.id

def remove_item_type(id):
    item_type = ItemType.query.get(id)
    if item_type:
        db.session.delete(item_type)
        db.session.commit()

def update_item_type(id, type, sub_type, min_amount, max_amount, wealth_indicator):
    item_type = ItemType.query.get(id)
    if item_type:
        item_type.type = type
        item_type.sub_type = sub_type
        item_type.min_amount = min_amount
        item_type.max_amount = max_amount
        item_type.wealth_indicator = wealth_indicator
        db.session.commit()

def add_item(name, current_price, min_price, max_price, current_amount, item_type_id, shop_id):
    new_item = Item(name=name, current_price=current_price, min_price=min_price, max_price=max_price, current_amount=current_amount, item_type_id=item_type_id, shop_id=shop_id)
    db.session.add(new_item)
    db.session.commit()
    return new_item.id

def remove_item(id):
    item = Item.query.get(id)
    if item:
        db.session.delete(item)
        db.session.commit()

def update_item(id, name, current_price, min_price, max_price, current_amount, item_type_id, shop_id):
    item = Item.query.get(id)
    if item:
        item.name = name
        item.current_price = current_price
        item.min_price = min_price
        item.max_price = max_price
        item.current_amount = current_amount
        item.item_type_id = item_type_id
        item.shop_id = shop_id
        db.session.commit()
