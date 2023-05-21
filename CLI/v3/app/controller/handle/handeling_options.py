from termcolor import colored
from sqlalchemy import inspect
from ...model.kingdom import Kingdom
from ...model.city import City
from ...model.shop import Shop
from ...model.item import Item
from ...model.item_type import ItemType
from ...model.shop_type import ShopType
import os

def clear_terminal():
    _ = os.system("clear")

def add_entity(session, entity_class, context):
    entity_attributes = {}
    entity_columns = [column.key for column in entity_class.__table__.columns if column.key != 'id']

    parent_entity_name = get_parent_entity_name(entity_columns)
    if parent_entity_name:
        parent_entity = get_parent_entity(session, parent_entity_name, context)
        if parent_entity:
            entity_attributes[parent_entity_name.lower()] = parent_entity
            entity_columns.remove(f'{parent_entity_name.lower()}_id')

    for column in entity_columns:
        if column not in entity_attributes:
            value = get_column_value(session, entity_class, column)
            entity_attributes[column] = value

    new_entity = entity_class(**entity_attributes)
    session.add(new_entity)
    session.commit()
    print(colored(f"{entity_class.__name__} added successfully!", 'green'))
    clear_terminal()


def get_parent_entity_name(entity_columns):
    for column_name in entity_columns:
        if column_name.endswith('_id'):
            return column_name[:-3].capitalize()
    return None


def get_parent_entity(session, parent_entity_name, context):
    entity_mapping = {
    "Kingdom": Kingdom,
    "City": City,
    "Shop": Shop,
    "Item": Item,
    "ItemType": ItemType,
    "ShopType": ShopType
    }
    parent_entity_name_in_context = context.get(parent_entity_name)
    if parent_entity_name_in_context:
        parent_entity_class = entity_mapping[parent_entity_name]
        return session.query(parent_entity_class).filter_by(name=parent_entity_name_in_context).first()
    return None


def get_column_value(session, entity_class, column):
    if column == 'name':
        return get_unique_name(session, entity_class)
    else:
        return input(colored(f"{entity_class.__name__} {column}:", attrs=['bold']))


def get_unique_name(session, entity_class):
    while True:
        name = input(colored(f"{entity_class.__name__} name:", attrs=['bold']))
        existing_entity = session.query(entity_class).filter_by(name=name).first()
        if existing_entity:
            print(colored("Name already exists. Please enter a different name.", 'red'))
        else:
            return name

def get_foreign_key_column(entity_class, parent_entity_class):
    foreign_key_columns = []
    for column in entity_class.__table__.columns:
        if column.foreign_keys:
            for foreign_key in column.foreign_keys:
                if foreign_key.column.table.name == parent_entity_class.__tablename__:
                    foreign_key_columns.append(column)
    if not foreign_key_columns:
        raise ValueError(f"No foreign key columns found in {entity_class.__name__} referencing {parent_entity_class.__name__}")
    return foreign_key_columns[0]


def show_entities(session, entity_class, parent_entity):
    if parent_entity:
        parent_entity_id_field = get_foreign_key_column(entity_class, parent_entity.__class__)
        entities = session.query(entity_class).filter(getattr(entity_class, parent_entity_id_field.key) == parent_entity.id).all()
    else:
        entities = session.query(entity_class).all()

    if not entities:
        print(colored(f"No {entity_class.__name__} entities found.", 'red'))
    else:
        print(colored(f"Available {entity_class.__name__} entities:", 'cyan', attrs=['bold']))
        for entity_obj in entities:
            print(colored(entity_obj.name, 'yellow'))
        print("")
