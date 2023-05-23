from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    current_price = Column(Float, nullable=False)
    min_price = Column(Float, nullable=False)
    max_price = Column(Float, nullable=False)
    current_amount = Column(Float, nullable=False)
    item_type_id = Column(Integer, ForeignKey('item_types.id'), nullable=False)
    shop_id = Column(Integer, ForeignKey('shops.id'))  # Add the foreign key to Shop

    shop = relationship("Shop", back_populates="items")  # Define the relationship with Shop

    def __repr__(self):
        return f"<Item(name={self.name}, current_price={self.current_price}, min_price={self.min_price}, max_price={self.max_price}, current_amount={self.current_amount}, shop={self.shop})>"