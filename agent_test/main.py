import random
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Step 1: Set up the Database
engine = create_engine('sqlite:///simulation.sqlite')
Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    temperature = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Step 2: Implement Agent and Simulation Logic
class WeatherAgent:
    def __init__(self, city):
        self.city = city

    def update_weather(self):
        self.city.temperature = random.randint(0, 40)

def run_simulation():
    cities = session.query(City).all()
    agents = [WeatherAgent(city) for city in cities]

    num_steps = 10

    for step in range(num_steps):
        for agent in agents:
            agent.update_weather()
            session.add(agent.city)  # Add each city individually to the session
            session.commit()

    cities = session.query(City).all()  # Fetch updated city data from the database

    for city in cities:
        print(f"{city.name}: {city.temperature}°C")

if __name__ == '__main__':
    run_simulation()
