from sqlalchemy import create_engine
from app.model.tables import Base
from termcolor import colored

DATABASE_NAME = "virtual_economy.sqlite"
engine = create_engine("sqlite:///" + DATABASE_NAME)


def init_db():
    Base.metadata.create_all(bind=engine)
    print(colored("Database created successfully.", "green"))