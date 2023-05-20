from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    shop_type = Column(Integer, ForeignKey('shop_types.id'), nullable=False)
    shop_owner = Column(Integer, ForeignKey('shop_owner.id'))
    


