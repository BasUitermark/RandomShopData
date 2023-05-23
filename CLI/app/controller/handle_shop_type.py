from base_handler import BaseHandler
from model.shop_type import ShopType

class ShopTypeHandler(BaseHandler):
    def add(self, session, shop_type):
        session.add(shop_type)
        session.commit()

    def update(self, session, shop_type_id, new_data):
        shop_type = session.query(ShopType).filter(ShopType.id == shop_type_id).first()
        for key, value in new_data.items():
            setattr(shop_type, key, value)
        session.commit()

    def delete(self, session, shop_type_id):
        shop_type = session.query(ShopType).filter(ShopType.id == shop_type_id).first()
        session.delete(shop_type)
        session.commit()

    def select(self, session, shop_type_id):
        shop_type = session.query(ShopType).filter(ShopType.id == shop_type_id).first()
        return shop_type

    def select_all(self, session):
        shop_types = session.query(ShopType).all()
        return shop_types