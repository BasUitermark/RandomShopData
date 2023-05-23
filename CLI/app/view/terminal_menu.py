from simple_term_menu import TerminalMenu
import os
from termcolor import colored
from time import sleep

def create_menu(title, menu_entries, color='yellow'):
    menu_cursor = "> "
    menu_cursor_style = ("fg_yellow", "bold")
    menu_highlight_style = ("fg_blue", "bold")

    print(colored(title, color, attrs=['bold']))
    return TerminalMenu(menu_entries=menu_entries,
                        menu_cursor=menu_cursor,
                        menu_cursor_style=menu_cursor_style,
                        menu_highlight_style=menu_highlight_style)

def clear_terminal():
    _ = os.system("clear")