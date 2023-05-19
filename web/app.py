# app.py
from flask import Flask, request, jsonify
from flask import request
from models import db, Country, City, Shop, ItemType, Item
import services
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/add_country', methods=['POST'])
def add_country():
    name = request.json['name']
    country_id = services.add_country(name)
    return jsonify({'status': 'Country added successfully', 'country_id': country_id})

@app.route('/remove_country/<int:id>', methods=['DELETE'])
def remove_country(id):
    services.remove_country(id)
    return jsonify({'status': 'Country removed successfully'})

@app.route('/update_country/<int:id>', methods=['PUT'])
def update_country(id):
    name = request.json['name']
    services.update_country(id, name)
    return jsonify({'status': 'Country updated successfully'})

@app.route('/add_city', methods=['POST'])
def add_city():
    name = request.json['name']
    population = request.json['population']
    wealth_indicator = request.json['wealth_indicator']
    country_id = request.json['country_id']
    city_id = services.add_city(name, population, wealth_indicator, country_id)
    return jsonify({'status': 'City added successfully', 'city_id': city_id})

@app.route('/remove_city/<int:id>', methods=['DELETE'])
def remove_city(id):
    services.remove_city(id)
    return jsonify({'status': 'City removed successfully'})

@app.route('/update_city/<int:id>', methods=['PUT'])
def update_city(id):
    name = request.json['name']
    population = request.json['population']
    wealth_indicator = request.json['wealth_indicator']
    country_id = request.json['country_id']
    services.update_city(id, name, population, wealth_indicator, country_id)
    return jsonify({'status': 'City updated successfully'})

def add_shop():
    name = request.json['name']
    city_id = request.json['city_id']
    shop_id = services.add_shop(name, city_id)
    return jsonify({'status': 'Shop added successfully', 'shop_id': shop_id})

@app.route('/remove_shop/<int:id>', methods=['DELETE'])
def remove_shop(id):
    services.remove_shop(id)
    return jsonify({'status': 'Shop removed successfully'})

@app.route('/update_shop/<int:id>', methods=['PUT'])
def update_shop(id):
    name = request.json['name']
    city_id = request.json['city_id']
    services.update_shop(id, name, city_id)
    return jsonify({'status': 'Shop updated successfully'})

@app.route('/add_item_type', methods=['POST'])
def add_item_type():
    type = request.json['type']
    sub_type = request.json['sub_type']
    min_amount = request.json['min_amount']
    max_amount = request.json['max_amount']
    wealth_indicator = request.json['wealth_indicator']
    item_type_id = services.add_item_type(type, sub_type, min_amount, max_amount, wealth_indicator)
    return jsonify({'status': 'Item type added successfully', 'item_type_id': item_type_id})

@app.route('/remove_item_type/<int:id>', methods=['DELETE'])
def remove_item_type(id):
    services.remove_item_type(id)
    return jsonify({'status': 'Item type removed successfully'})

@app.route('/update_item_type/<int:id>', methods=['PUT'])
def update_item_type(id):
    type = request.json['type']
    sub_type = request.json['sub_type']
    min_amount = request.json['min_amount']
    max_amount = request.json['max_amount']
    wealth_indicator = request.json['wealth_indicator']
    services.update_item_type(id, type, sub_type, min_amount, max_amount, wealth_indicator)
    return jsonify({'status': 'Item type updated successfully'})

@app.route('/add_item', methods=['POST'])
def add_item():
    name = request.json['name']
    current_price = request.json['current_price']
    min_price = request.json['min_price']
    max_price = request.json['max_price']
    current_amount = request.json['current_amount']
    item_type_id = request.json['item_type_id']
    shop_id = request.json['shop_id']
    item_id = services.add_item(name, current_price, min_price, max_price, current_amount, item_type_id, shop_id)
    return jsonify({'status': 'Item added successfully', 'item_id': item_id})

@app.route('/remove_item/<int:id>', methods=['DELETE'])
def remove_item(id):
    services.remove_item(id)
    return jsonify({'status': 'Item removed successfully'})

@app.route('/update_item/<int:id>', methods=['PUT'])
def update_item(id):
    name = request.json['name']
    current_price = request.json['current_price']
    min_price = request.json['min_price']
    max_price = request.json['max_price']
    current_amount = request.json['current_amount']
    item_type_id = request.json['item_type_id']
    shop_id = request.json['shop_id']
    services.update_item(id, name, current_price, min_price, max_price, current_amount, item_type_id, shop_id)
    return jsonify({'status': 'Item updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)