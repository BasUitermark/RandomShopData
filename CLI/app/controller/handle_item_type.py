from .base_handler import BaseHandler
from model.item_type import ItemType

class ItemTypeHandler(BaseHandler):
    model = ItemType

    def add(self, session, item_type, sub_type, min_amount, max_amount, wealth_indicator):
        item_type = ItemType(
            item_type=item_type, 
            sub_type=sub_type, 
            min_amount=min_amount, 
            max_amount=max_amount, 
            wealth_indicator=wealth_indicator)
        session.add(item_type)
        session.commit()

    def update(self, session, item_type_id, item_type=None, sub_type=None, min_amount=None, max_amount=None, wealth_indicator=None):
        item_type = session.query(ItemType).filter(ItemType.id == item_type_id).one()

        if item_type is not None:
            item_type.item_type = item_type

        if sub_type is not None:
            item_type.sub_type = sub_type

        if min_amount is not None:
            item_type.min_amount = min_amount

        if max_amount is not None:
            item_type.max_amount = max_amount

        if wealth_indicator is not None:
            item_type.wealth_indicator = wealth_indicator

        session.commit()


    def delete(self, session, item_type_id):
        item_type = session.query(ItemType).filter(ItemType.id == item_type_id).first()
        session.delete(item_type)
        session.commit()

    def select(self, session, item_type_id):
        item_type = session.query(ItemType).filter(ItemType.id == item_type_id).first()
        return item_type

    def select_all(self, session):
        item_types = session.query(ItemType).all()
        return item_types
    
    def select_by_name(self, session, shop_name):
        shop = session.query(ItemType).filter(ItemType.item_type == shop_name).first()
        return shop