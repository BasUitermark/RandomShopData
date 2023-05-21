from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    wealth = Column(Float, nullable=False)
    demand = Column(Integer)
    supply = Column(Integer)
    economic_strength = Column(Float)
    political_stability = Column(Float)
    inflation_rate = Column(Float)
    interest_rate = Column(Float)

    kingdom_id = Column(Integer, ForeignKey('kingdoms.id'))
    kingdom = relationship("Kingdom", back_populates="cities")  # Adjust the relationship configuration here

    shops = relationship("Shop", back_populates="city")

    sub_entities = {"Shops": "Shop"}

    def __repr__(self):
        return f"<City(name={self.name}, population={self.population}, wealth={self.wealth}, \
                demand={self.demand}, supply={self.supply}, \
                economic_strength={self.economic_strength}, politcal_stability={self.political_stability}, \
                inflation_rate={self.inflation_rate}, interest_rate={self.interest_rate}, shops={self.shops})>"
