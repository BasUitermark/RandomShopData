from app.model.kingdom import Kingdom
from .handeling_options import add_entity
from .handeling_options import show_entities

def handle_kingdom(action, session, context, entity, parent_entity):
    entity_class = eval(entity)
    print("Handeling Kingdom")
    if action == "Add":
        add_entity(session, Kingdom, context)
    elif action == "Select":
        show_entities(session, entity_class, parent_entity)
    # elif action == 'Update':
    #     update_kingdom(session)
    # elif action == 'Delete':
    #     remove_kingdom(session)