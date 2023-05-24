from controller.handle_shop import ShopHandler
from controller.handle_city import CityHandler
from controller.handle_kingdom import KingdomHandler

def display_hierarchical_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_handler = ShopHandler()

    # Get all kingdoms
    kingdoms = kingdom_handler.select_all(session)
    for kingdom in kingdoms:
        print(kingdom.name)
        
        # Get all cities in the current kingdom
        cities = city_handler.select_by_kingdom(session, kingdom.id)
        for city in cities:
            print("\t", city.name)
            
            # Get all shops in the current city
            shops = shop_handler.select_by_city(session, city.id)
            for shop in shops:
                print("\t\t", shop.name)
