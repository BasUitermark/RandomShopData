from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from termcolor import colored
from app.model.tables import Base

DATABASE_NAME = "virtual_economy.sqlite"
engine = create_engine("sqlite:///" + DATABASE_NAME)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(bind=engine)
    print(colored("Database created successfully.", "green"))