from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from termcolor import colored

DATABASE_NAME = "virtual_economy.sqlite"
engine = create_engine("sqlite:///" + DATABASE_NAME)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    population = Column(Integer)
    wealth_indicator = Column(Float)
    country_id = Column(Integer, ForeignKey("countries.id"))
    country = relationship("Country")


class Shop(Base):
    __tablename__ = "shops"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))
    city = relationship("City")


class ItemType(Base):
    __tablename__ = "item_types"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    sub_type = Column(String)
    min_amount = Column(Integer)
    max_amount = Column(Integer)
    wealth_indicator = Column(Float)


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    current_price = Column(Float)
    min_price = Column(Float)
    max_price = Column(Float)
    current_amount = Column(Integer)
    item_type_id = Column(Integer, ForeignKey("item_types.id"))
    item_type = relationship("ItemType")
    shop_id = Column(Integer, ForeignKey("shops.id"))
    shop = relationship("Shop")


def create_database():
    Base.metadata.create_all(bind=engine)
    print(colored("Database created successfully.", "green"))
