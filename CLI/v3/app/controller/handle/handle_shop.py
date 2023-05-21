from app.model.shop import Shop
from .handeling_options import add_entity

def handle_shop(action, session, context):
    if action == "Add":
        add_entity(session, Shop, context)