from app.model.city import City
from app.model.kingdom import Kingdom
from .handeling_options import add_entity
from .handeling_options import show_entities

def handle_city(action, session, context, entity, parent_entity):
    entity_class = City
    if action == "Add":
        add_entity(session, City, context)
    elif action == "Select":
        show_entities(session, entity_class, parent_entity)
        
