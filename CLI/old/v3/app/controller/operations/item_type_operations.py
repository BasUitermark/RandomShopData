from termcolor import colored
from sqlalchemy.orm import Session
from app.model.item_type import ItemType

def add_item_type(session: Session, item_type: str, sub_type: str, min_amount: float, max_amount: float, wealth_indicator: float):
    new_item_type = ItemType(item_type=item_type, sub_type=sub_type, min_amount=min_amount, max_amount=max_amount, wealth_indicator=wealth_indicator)
    session.add(new_item_type)
    session.commit()
    return colored(f"Added item type {item_type} with sub type {sub_type}", "green")

def delete_item_type(session: Session, item_type_id: int):
    item_type = session.query(ItemType).get(item_type_id)
    if item_type is None:
        return colored(f"No item type found with id {item_type_id}", "red")
    session.delete(item_type)
    session.commit()
    return colored(f"Deleted item type {item_type.item_type}", "green")

def update_item_type(session: Session, item_type_id: int, item_type: str = None, sub_type: str = None, min_amount: float = None, max_amount: float = None, wealth_indicator: float = None):
    item_type_obj = session.query(ItemType).get(item_type_id)
    if item_type_obj is None:
        return colored(f"No item type found with id {item_type_id}", "red")

    if item_type is not None:
        item_type_obj.item_type = item_type
    if sub_type is not None:
        item_type_obj.sub_type = sub_type
    if min_amount is not None:
        item_type_obj.min_amount = min_amount
    if max_amount is not None:
        item_type_obj.max_amount = max_amount
    if wealth_indicator is not None:
        item_type_obj.wealth_indicator = wealth_indicator

    session.commit()
    return colored(f"Updated item type {item_type_obj.item_type}", "green")
