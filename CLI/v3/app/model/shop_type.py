from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class ShopType(Base):
    __tablename__ = 'shop_types'

    id = Column(Integer, primary_key=True)
    shop_type = Column(String, nullable=False)