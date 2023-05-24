from database.initialize_database import init_db
from view.select_view import clear_terminal
from view.terminal_menu import display_menu
from database.database_session import session

from termcolor import colored
from time import sleep
import os

def main():
    if not os.path.exists("virtual_economy.sqlite"):
        print(colored("Database not found. Creating a new database...", 'yellow'))
        init_db()
    print(colored("Welcome to", attrs=['bold']))
    print(colored("DnD Virtual Economy", 'yellow', attrs=['bold']))
    display_menu(session)
    sleep(1)

if __name__ == "__main__":
    clear_terminal()
    main()