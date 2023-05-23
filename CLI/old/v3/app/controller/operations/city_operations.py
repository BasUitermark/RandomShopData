from termcolor import colored
from sqlalchemy.orm import Session
from app.model.kingdom import Kingdom
from app.model.city import City

def add_city(session: Session, kingdom_id: int, name: str, demand: int, supply: int):
    kingdom = session.query(Kingdom).get(kingdom_id)
    if kingdom is None:
        return colored(f"No kingdom found with id {kingdom_id}", "red")
        
    new_city = City(kingdom_id=kingdom.id, name=name, demand=demand, supply=supply)
    session.add(new_city)
    session.commit()
    return colored(f"City {name} added successfully under kingdom {kingdom.name}", "green")

def remove_city(session: Session, city_id: int):
    city = session.query(City).get(city_id)
    if city is None:
        return colored(f"No city found with id {city_id}", "red")

    session.delete(city)
    session.commit()
    return colored(f"City {city.name} removed successfully", "green")

def update_city(session: Session, city_id: int, name: str = None, demand: int = None, supply: int = None):
    city = session.query(City).get(city_id)
    if city is None:
        return colored(f"No city found with id {city_id}", "red")
        
    if name is not None:
        city.name = name
    if demand is not None:
        city.demand = demand
    if supply is not None:
        city.supply = supply

    session.commit()
    return colored(f"City {city.name} updated successfully", "green")
