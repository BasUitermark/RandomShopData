from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class ItemType(Base):
    __tablename__ = 'item_types'

    id = Column(Integer, primary_key=True)
    item_type = Column(String, nullable=False)
    sub_type = Column(String, nullable=False)
    min_amount = Column(Float, nullable=False)
    max_amount = Column(Float, nullable=False)
    wealth_indicator = Column(Float, nullable=False)