from controller.handle_shop import ShopHandler
from controller.handle_city import CityHandler
from controller.handle_kingdom import KingdomHandler
from termcolor import colored

def display_hierarchical_view(session):
    # Create handlers
    kingdom_handler = KingdomHandler()
    city_handler = CityHandler()
    shop_handler = ShopHandler()

    # Get all kingdoms
    kingdoms = kingdom_handler.select_all(session)
    for kingdom in kingdoms:
        print(colored(">", attrs=['bold']),colored(kingdom.name, 'green', attrs=['bold']))
        
        # Get all cities in the current kingdom
        cities = city_handler.select_by_kingdom(session, kingdom.id)
        for city in cities:
            print(colored(">\t", attrs=['bold']), colored(city.name, 'green', attrs=['bold']))
            
            # Get all shops in the current city
            shops = shop_handler.select_by_city(session, city.id)
            for shop in shops:
                print(colored(">\t\t", attrs=['bold']), colored(shop.name, 'green', attrs=['bold']))
