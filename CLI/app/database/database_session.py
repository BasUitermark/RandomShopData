from sqlalchemy.orm import sessionmaker
from initialize_database import engine

Session = sessionmaker(bind=engine)
session = Session()