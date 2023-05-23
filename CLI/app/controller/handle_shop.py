from base_handler import BaseHandler
from model.shop import Shop

class ShopHandler(BaseHandler):
    def add(self, session, shop_name, shop_type_id, city_id):
        new_shop = Shop(name=shop_name, shop_type_id=shop_type_id, city_id=city_id)
        session.add(new_shop)
        session.commit()

    def update(self, session, shop_id, name=None, shop_type_id=None, city_id=None):
        shop = session.query(Shop).filter(Shop.id == shop_id).one()
        
        if name is not None:
            shop.name = name
            
        if shop_type_id is not None:
            shop.shop_type_id = shop_type_id
            
        if city_id is not None:
            shop.city_id = city_id
        session.commit()

    def delete(self, session, shop_id):
        shop = session.query(Shop).filter(Shop.id == shop_id).first()
        session.delete(shop)
        session.commit()

    def select(self, session, shop_id):
        shop = session.query(Shop).filter(Shop.id == shop_id).first()
        return shop

    def select_by_city(self, session, city_id):
        cities = session.query(Shop).filter(Shop.city_id == city_id).all()
        return cities

    def select_all(self, session):
        cities = session.query(Shop).all()
        return cities