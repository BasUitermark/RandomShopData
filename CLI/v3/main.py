import os
from termcolor import colored
from initialize_database import init_db
from 

def main():
    if not os.path.exists("virtual_economy.sqlite"):
        print(colored("Database not found. Creating a new database...", 'yellow'))
        init_db()
    display_menu()

if __name__ == "__main__":
    main()