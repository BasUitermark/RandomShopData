import os
from termcolor import colored
from CLI.app.database.initialize_database import init_db
from app.view.terminal_menu import clear_terminal
from time import sleep

def main():
    if not os.path.exists("virtual_economy.sqlite"):
        print(colored("Database not found. Creating a new database...", 'yellow'))
        init_db()
    print(colored("Welcome to", attrs=['bold']))
    print(colored("DnD Virtual Economy", 'yellow', attrs=['bold']))
    sleep(1)

if __name__ == "__main__":
    clear_terminal()
    main()