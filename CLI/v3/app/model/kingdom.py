from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class Kingdom(Base):
    __tablename__ = 'kingdoms'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    demand = Column(Integer)
    supply = Column(Integer)
    economic_strength = Column(Float)
    political_stability = Column(Float)
    inflation_rate = Column(Float)
    interest_rate = Column(Float)
    
    cities = relationship("City", back_populates="kingdom")
    
    def __repr__(self):
        return f"<Kingdom(name={self.name}, \
                demand={self.demand}, supply={self.supply}, \
                economic_strength={self.economic_strength}, politcal_stability={self.political_stability}, \
                inflation_rate={self.inflation_rate}, interest_rate={self.interest_rate}, \
                cities={self.cities})>"

# Base.metadata.tables[Kingdom.__tablename__] = Kingdom.__table__