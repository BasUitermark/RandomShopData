# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    wealth_indicator = db.Column(db.Float, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    country = db.relationship('Country')


class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    city = db.relationship('City')


class ItemType(db.Model):
    __tablename__ = 'item_types'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    sub_type = db.Column(db.String, nullable=False)
    min_amount = db.Column(db.Float, nullable=False)
    max_amount = db.Column(db.Float, nullable=False)
    wealth_indicator = db.Column(db.Float, nullable=False)


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    min_price = db.Column(db.Float, nullable=False)
    max_price = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, nullable=False)
    item_type_id = db.Column(db.Integer, db.ForeignKey('item_types.id'))
    item_type = db.relationship('ItemType')
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
    shop = db.relationship('Shop')
