from .base_handler import BaseHandler
from model.kingdom import Kingdom

class KingdomHandler(BaseHandler):
    def add(self, session, kingdom_name):
        new_kingdom = Kingdom(name=kingdom_name)
        session.add(new_kingdom)
        session.commit()

    def update(self, session, kingdom_id, name=None):
        kingdom = session.query(Kingdom).filter(Kingdom.id == kingdom_id).one()
        
        if name is not None:
            kingdom.name = name
        session.commit()

    def delete(self, session, kingdom_id):
        kingdom = session.query(Kingdom).filter(Kingdom.id == kingdom_id).first()
        session.delete(kingdom)
        session.commit()

    def select(self, session, kingdom_id):
        kingdom = session.query(Kingdom).filter(Kingdom.id == kingdom_id).first()
        return kingdom

    def select_all(self, session):
        kingdoms = session.query(Kingdom).all()
        return kingdoms