from .base_handler import BaseHandler
from model.city import City

class CityHandler(BaseHandler):
    def add(self, session, city_name, city_population, city_wealth, kingdom_id):
        new_city = City(name=city_name, population=city_population, wealth=city_wealth, kingdom_id=kingdom_id)
        session.add(new_city)
        session.commit()

    def update(self, session, shop_id, city_name=None, city_population=None, kingdom_id=None):
        city = session.query(City).filter(City.id == shop_id).one()
        
        if city_name is not None:
            city.name = city_name
            
        if city_population is not None:
            city.population = city_population
            
        if kingdom_id is not None:
            city.kingdom_id = kingdom_id
        session.commit()

    def delete(self, session, city_id):
        city = session.query(City).filter(City.id == city_id).first()
        session.delete(city)
        session.commit()

    def select(self, session, city_id):
        city = session.query(City).filter(City.id == city_id).first()
        return city
    
    def select_by_kingdom(self, session, kingdom_id):
        cities = session.query(City).filter(City.kingdom_id == kingdom_id).all()
        return cities

    def select_all(self, session):
        cities = session.query(City).all()
        return cities