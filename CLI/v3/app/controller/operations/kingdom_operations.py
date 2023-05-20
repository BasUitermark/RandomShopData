from termcolor import colored
from sqlalchemy.orm import Session
from app.model.kingdom import Kingdom

def add_kingdom(session: Session, name: str, demand: int, supply: int, economic_strength: float, political_stability: float, inflation_rate: float, interest_rate: float):
    new_kingdom = Kingdom(name=name, demand=demand, supply=supply, economic_strength=economic_strength, political_stability=political_stability, inflation_rate=inflation_rate, interest_rate=interest_rate)
    session.add(new_kingdom)
    session.commit()
    return colored(f"Kingdom {name} added successfully", "green")

def remove_kingdom(session: Session, kingdom_id: int):
    kingdom = session.query(Kingdom).get(kingdom_id)
    if kingdom is None:
        return colored(f"No kingdom found with id {kingdom_id}", "red")

    session.delete(kingdom)
    session.commit()
    return colored(f"Kingdom {kingdom.name} removed successfully", "green")

def update_kingdom(session: Session, kingdom_id: int, name: str = None, demand: int = None, supply: int = None, economic_strength: float = None, political_stability: float = None, inflation_rate: float = None, interest_rate: float = None):
    kingdom = session.query(Kingdom).get(kingdom_id)
    if kingdom is None:
        return colored(f"No kingdom found with id {kingdom_id}", "red")
        
    if name is not None:
        kingdom.name = name
    if demand is not None:
        kingdom.demand = demand
    if supply is not None:
        kingdom.supply = supply
    if economic_strength is not None:
        kingdom.economic_strength = economic_strength
    if political_stability is not None:
        kingdom.political_stability = political_stability
    if inflation_rate is not None:
        kingdom.inflation_rate = inflation_rate
    if interest_rate is not None:
        kingdom.interest_rate = interest_rate

    session.commit()
    return colored(f"Kingdom {kingdom.name} updated successfully", "green")
