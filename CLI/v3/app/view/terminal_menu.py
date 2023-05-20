from simple_term_menu import TerminalMenu

def create_menu(title, menu_entries):
    menu_cursor = "> "
    menu_cursor_style = ("fg_yellow", "bold")
    menu_highlight_style = ("fg_blue", "bold")

    return TerminalMenu(menu_entries=menu_entries,
                        title=title,
                        menu_cursor=menu_cursor,
                        menu_cursor_style=menu_cursor_style,
                        menu_highlight_style=menu_highlight_style)
    
def handle_manage_operations():
    while True:
        menu_entries = ["Kingdoms", "Cities", "Shops", "Items in Shops", "Item Types", "Shop Types", "Go back"]
        menu = create_menu("Manage Data", menu_entries)
        menu_choice = menu.show()

        if menu_choice == len(menu_entries) - 1:  # "Go back" selected
            break
        else:
            handle_manage_for(menu_entries[menu_choice])

def handle_manage_for(entity):
    while True:
        menu_entries = ["Add", "Delete", "Update", "Go back"]
        menu = create_menu(f"CRUD Operations for {entity}", menu_entries)
        menu_choice = menu.show()

        if menu_choice == len(menu_entries) - 1:  # "Go back" selected
            break
        elif menu_choice == 0:  # "Add" selected
            # Call your add function here
            pass
        elif menu_choice == 1:  # "Delete" selected
            # Call your delete function here
            pass
        elif menu_choice == 2:  # "Update" selected
            # Call your update function here
            pass

def handle_show_data():
    # Add your code to show data here
    pass

def handle_import_export():
    # Add your code to handle import/export here
    pass

def display_menu():
    while True:
        menu_entries = ["CRUD Operations", "Show Data", "Import/Export", "Exit"]
        menu = create_menu("Main Menu", menu_entries)
        menu_choice = menu.show()

        if menu_choice == 0:  # "CRUD Operations" selected
            handle_manage_operations()
        elif menu_choice == 1:  # "Show Data" selected
            handle_show_data()
        elif menu_choice == 2:  # "Import/Export" selected
            handle_import_export()
        elif menu_choice == 3:  # "Exit" selected
            break