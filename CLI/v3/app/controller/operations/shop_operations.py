from termcolor import colored
from sqlalchemy.orm import Session
from app.model.shop import Shop
from app.model.city import City
from app.model.shop_type import ShopType

def add_shop(session: Session, city_id: int, name: str, shop_type_id: int):
    city = session.query(City).get(city_id)
    shop_type = session.query(ShopType).get(shop_type_id)
    if city is None:
        return colored(f"No city found with id {city_id}", "red")
    if shop_type is None:
        return colored(f"No shop type found with id {shop_type_id}", "red")

    new_shop = Shop(city_id=city.id, name=name, shop_type=shop_type.id)
    session.add(new_shop)
    session.commit()
    return colored(f"Added shop {name} to city {city.name} with shop type {shop_type.shop_type}", "green")

def delete_shop(session: Session, shop_id: int):
    shop = session.query(Shop).get(shop_id)
    if shop is None:
        return colored(f"No shop found with id {shop_id}", "red")
    session.delete(shop)
    session.commit()
    return colored(f"Deleted shop {shop.name}", "green")

def update_shop(session: Session, shop_id: int, name: str = None, shop_type_id: int = None):
    shop = session.query(Shop).get(shop_id)
    if shop is None:
        return colored(f"No shop found with id {shop_id}", "red")

    if name is not None:
        shop.name = name
    if shop_type_id is not None:
        shop_type = session.query(ShopType).get(shop_type_id)
        if shop_type is None:
            return colored(f"No shop type found with id {shop_type_id}", "red")
        shop.shop_type = shop_type.id

    session.commit()
    return colored(f"Updated shop {shop.name}", "green")
