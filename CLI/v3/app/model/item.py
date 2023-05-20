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

	shop_id = Column(Integer, ForeignKey('shops.id'))
