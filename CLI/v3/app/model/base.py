from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey
Base = declarative_base()

# Import all models so they are part of the Base metadata and tables will be created for them
from .kingdom import Kingdom
from .city import City
from .shop import Shop
from .item import Item
from .item_type import ItemType
