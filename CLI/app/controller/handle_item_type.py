from base_handler import BaseHandler
from model.item_type import ItemType

class ItemTypeHandler(BaseHandler):
    def add(self, session, item_type):
        session.add(item_type)
        session.commit()

    def update(self, session, item_type_id, new_data):
        item_type = session.query(ItemType).filter(ItemType.id == item_type_id).first()
        for key, value in new_data.items():
            setattr(item_type, key, value)
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