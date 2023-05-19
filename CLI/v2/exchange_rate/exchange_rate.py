from ..database.database_operation import session, City, Item, ItemType


def calculate_exchange_rate(city_id, item_id):
    city = session.query(City).filter_by(id=city_id).first()
    item = session.query(Item).filter_by(id=item_id).first()
    if city and item:
        city_wealth = city.wealth_indicator
        city_population = city.population
        item_type_wealth = item.item_type.wealth_indicator
        item_min_amount = item.item_type.min_amount
        item_max_amount = item.item_type.max_amount
        exchange_rate = city_wealth * city_population * item_type_wealth * (item_min_amount + item_max_amount)
        return exchange_rate
    return None
