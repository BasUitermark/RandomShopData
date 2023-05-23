from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
    
class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    shop_type_id = Column(Integer, ForeignKey('shop_types.id'), nullable=False)
    shop_type = relationship("ShopType")
    items = relationship("Item", back_populates="shop")
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship("City", back_populates="shops")  # Adjust the relationship configuration here

    sub_entities = {"Items": "Item"}

    def __repr__(self):
        return f"<Shop(name={self.name}, city={self.city}, shop_type={self.shop_type}, items={self.items})>"