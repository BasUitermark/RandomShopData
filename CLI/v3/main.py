from sqlalchemy.exc import OperationalError
from termcolor import colored
from initialize_database import init_db, Session

def main():
    try:
        session = Session()
        session.close()
    except OperationalError:
        print(colored("Database not found. Creating a new database...", 'yellow'))
        init_db()
    
    # Continue with rest of your application

if __name__ == "__main__":
    main()