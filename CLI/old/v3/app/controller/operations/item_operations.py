from termcolor import colored
from sqlalchemy.orm import Session
from app.model.item import Item
from app.model.shop import Shop
from app.model.item_type import ItemType

def add_item(session: Session, shop_id: int, name: str, current_price: float, min_price: float, max_price: float, current_amount: float, item_type_id: int):
    shop = session.query(Shop).get(shop_id)
    item_type = session.query(ItemType).get(item_type_id)
    if shop is None:
        return colored(f"No shop found with id {shop_id}", "red")
    if item_type is None:
        return colored(f"No item type found with id {item_type_id}", "red")

    new_item = Item(shop_id=shop.id, name=name, current_price=current_price, min_price=min_price, max_price=max_price, current_amount=current_amount, item_type_id=item_type.id)
    session.add(new_item)
    session.commit()
    return colored(f"Added item {name} to shop {shop.name} with item type {item_type.item_type}", "green")

def delete_item(session: Session, item_id: int):
    item = session.query(Item).get(item_id)
    if item is None:
        return colored(f"No item found with id {item_id}", "red")
    session.delete(item)
    session.commit()
    return colored(f"Deleted item {item.name}", "green")

def update_item(session: Session, item_id: int, name: str = None, current_price: float = None, min_price: float = None, max_price: float = None, current_amount: float = None, item_type_id: int = None):
    item = session.query(Item).get(item_id)
    if item is None:
        return colored(f"No item found with id {item_id}", "red")

    if name is not None:
        item.name = name
    if current_price is not None:
        item.current_price = current_price
    if min_price is not None:
        item.min_price = min_price
    if max_price is not None:
        item.max_price = max_price
    if current_amount is not None:
        item.current_amount = current_amount
    if item_type_id is not None:
        item_type = session.query(ItemType).get(item_type_id)
        if item_type is None:
            return colored(f"No item type found with id {item_type_id}", "red")
        item.item_type_id = item_type.id

    session.commit()
    return colored(f"Updated item {item.name}", "green")
