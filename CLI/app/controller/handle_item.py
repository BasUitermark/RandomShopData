from base_handler import BaseHandler
from model.item import Item

class ItemHandler(BaseHandler):
    def add(self, session, item_name, current_price, min_price, max_price, current_amount, item_type_id, shop_id):
        new_item = Item(name=item_name, current_price=current_price, min_price=min_price, max_price=max_price, current_amount=current_amount, item_type_id=item_type_id, shop_id=shop_id)
        session.add(new_item)
        session.commit()

    def update(self, session, item_id, name=None, current_price=None, min_price=None, max_price=None, current_amount=None, item_type_id=None, shop_id=None):
        item = session.query(Item).filter(Item.id == item_id).one()

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
            item.item_type_id = item_type_id

        if shop_id is not None:
            item.shop_id = shop_id

        session.commit()

    def delete(self, session, item_id):
        item = session.query(Item).filter(Item.id == item_id).first()
        session.delete(item)
        session.commit()

    def select(self, session, item_id):
        item = session.query(Item).filter(Item.id == item_id).first()
        return item

    def select_all(self, session):
        items = session.query(Item).all()
        return items

    def select_by_shop(self, session, shop_id):
        items = session.query(Item).filter(Item.shop_id == shop_id).all()
        return items