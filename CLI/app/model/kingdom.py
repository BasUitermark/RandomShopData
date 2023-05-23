from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

trade_relationships = Table('trade_relationships', Base.metadata,
    Column('kingdom_id', Integer, ForeignKey('kingdoms.id'), primary_key=True),
    Column('trade_partner_id', Integer, ForeignKey('kingdoms.id'), primary_key=True)
)

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
    
    cities = relationship("City", back_populates="kingdom", cascade="all, delete-orphan")
    
    trade_partners = relationship('Kingdom', secondary=trade_relationships, 
                                  primaryjoin=id==trade_relationships.c.kingdom_id,
                                  secondaryjoin=id==trade_relationships.c.trade_partner_id,
                                  backref="trade_partnerships", single_parent=True, cascade="all, delete-orphan")
    
    sub_entities = {"Cities": "City"}
    
    def __repr__(self):
        return f"<Kingdom(name={self.name}, \
                demand={self.demand}, supply={self.supply}, \
                economic_strength={self.economic_strength}, politcal_stability={self.political_stability}, \
                inflation_rate={self.inflation_rate}, interest_rate={self.interest_rate}, \
                cities={self.cities})>"
