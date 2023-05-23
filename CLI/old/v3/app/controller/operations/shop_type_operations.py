from termcolor import colored
from sqlalchemy.orm import Session
from app.model.shop_type import ShopType

def add_shop_type(session: Session, shop_type: str):
    new_shop_type = ShopType(shop_type=shop_type)
    session.add(new_shop_type)
    session.commit()
    return colored(f"Added shop type {shop_type}", "green")

def delete_shop_type(session: Session, shop_type_id: int):
    shop_type = session.query(ShopType).get(shop_type_id)
    if shop_type is None:
        return colored(f"No shop type found with id {shop_type_id}", "red")
    session.delete(shop_type)
    session.commit()
    return colored(f"Deleted shop type {shop_type.shop_type}", "green")

def update_shop_type(session: Session, shop_type_id: int, shop_type: str = None):
    shop_type_obj = session.query(ShopType).get(shop_type_id)
    if shop_type_obj is None:
        return colored(f"No shop type found with id {shop_type_id}", "red")

    if shop_type is not None:
        shop_type_obj.shop_type = shop_type

    session.commit()
    return colored(f"Updated shop type {shop_type_obj.shop_type}", "green")
