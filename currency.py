import sqlite3
import matplotlib.pyplot as plt

class VirtualCurrency:
    def __init__(self, initial_value=1.0):
        self.value = initial_value
        self.population_weight = 0.3
        self.import_export_weight = 0.2
        self.wealth_indicator_weight = 0.2
        self.shop_prices_weight = 0.1
        self.potential_sales_weight = 0.2
        self.history = []

    def update_value_based_on_population(self, population):
        population_factor = population * 0.01
        self.value += population_factor * self.population_weight

    def update_value_based_on_import_export(self, import_value, export_value):
        net_balance = import_value - export_value
        self.value += net_balance * 0.01 * self.import_export_weight

    def update_value_based_on_wealth_indicator(self, wealth_indicator):
        self.value += wealth_indicator * 0.01 * self.wealth_indicator_weight

    def update_value_based_on_shop_prices(self, shop_prices):
        price_factor = (1 - shop_prices)  # Assuming shop_prices is a value between 0 and 1
        self.value += price_factor * self.shop_prices_weight

    def update_value_based_on_potential_sales(self, potential_sales):
        self.value += potential_sales * 0.01 * self.potential_sales_weight

    def buy_currency(self, amount):
        self.value += amount

    def sell_currency(self, amount):
        self.value -= amount

    def plot_history(self):
        x = range(len(self.history))
        y = [data[0] for data in self.history]
        plt.plot(x, y)
        plt.xlabel('Time')
        plt.ylabel('Currency Value')
        plt.title('Currency Value Over Time')
        plt.show()
        
def simulate():
    currency = VirtualCurrency()
    create_table_countries()
    create_table_cities()
    create_table_shops()
    create_table_items()
    create_table_item_types()

    while True:
        conn = sqlite3.connect('mydatabase.sqlite')
        c = conn.cursor()

        c.execute("SELECT * FROM countries")
        countries = c.fetchall()

        for country in countries:
            country_id, country_name = country

            c.execute("SELECT * FROM cities WHERE country_id=?", (country_id,))
            cities = c.fetchall()

            for city in cities:
                city_id, city_name, population, wealth_factor, _ = city

                c.execute("SELECT * FROM shops WHERE city_id=?", (city_id,))
                shops = c.fetchall()

                for shop in shops:
                    shop_id, shop_name, _ = shop

                    c.execute("SELECT * FROM items WHERE shop_id=?", (shop_id,))
                    items = c.fetchall()

                    # Update item prices and stock based on currency value and wealth factor
                    for item in items:
                        item_id, item_name, min_price, max_price, stock, _, item_type_id = item

                        c.execute("SELECT wealth_factor FROM item_types WHERE id=?", (item_type_id,))
                        wealth_factor = c.fetchone()[0]

                        # Update item price based on currency value and wealth factor
                        min_price *= currency.value * wealth_factor
                        max_price *= currency.value * wealth_factor

                        # Update item stock based on currency value and wealth factor
                        stock *= int(currency.value * wealth_factor)

                        c.execute("UPDATE items SET min_price=?, max_price=?, stock=? WHERE id=?",
                                  (min_price, max_price, stock, item_id))

                conn.commit()

        conn.close()

        # Display current value
        print(f"Current Value: {currency.value}")

        # Wait for a certain period before the next iteration
        time.sleep(5)  # Adjust the sleep duration as desired