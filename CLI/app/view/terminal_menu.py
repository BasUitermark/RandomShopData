from .kingdom_view import manage_kingdom
from .city_view import manage_city
from .shop_view import manage_shop
from .item_view import manage_item
from .item_type_view import manage_item_type
from .shop_type_view import manage_shop_type
from .import_view import manage_import
from .export_view import manage_export_csv, manage_export_pdf
from .display_hierarchy_view import display_hierarchical_view
from .select_view import basic_menu, clear_terminal

def handle_manage_operations(session):
    while True:
        main_menu_entries = ["Kingdom", "City", "Shop", "Item", "Item Type", "Shop Type", "Go back"]
        main_menu = basic_menu("Manage World", main_menu_entries)
        main_menu_choice = main_menu.show()
        clear_terminal()

        if main_menu_choice == 0:  # "Manage Kingdom"
            manage_kingdom(session)

        elif main_menu_choice == 1:  # "Manage City"
            manage_city(session)

        elif main_menu_choice == 2:  # "Manage Shop"
            manage_shop(session)

        elif main_menu_choice == 3:  # "Manage Item"
            manage_item(session)

        elif main_menu_choice == 4:  # "Manage Item Type"
            manage_item_type(session)
            
        elif main_menu_choice == 5:  # "Manage Shop Type"
            manage_shop_type(session)

        elif main_menu_choice == 6:  # "Go back"
            break


def handle_import_export(session):
    while True:
        main_menu_entries = ["Import", "Export CSV", "Export PDF", "Go back"]
        main_menu = basic_menu("Import & Export Item Lists", main_menu_entries)
        main_menu_choice = main_menu.show()
        clear_terminal()

        if main_menu_choice == 0:  # "Manage Import"
            manage_import(session)

        elif main_menu_choice == 1:  # "Manage Export CSV"
            manage_export_csv(session)
            
        elif main_menu_choice == 2:  # "Manage Export PDF"
            manage_export_pdf(session)

        elif main_menu_choice == 3:  # "Go back"
            break



def display_menu(session):
    clear_terminal()
    while True:
        menu_entries = ["Manage World", "Show Data", "Import/Export", "Exit"]
        menu = basic_menu("Main Menu", menu_entries)
        menu_choice = menu.show()
        clear_terminal()

        if menu_choice == 0:  # "Management Operations" selected
            handle_manage_operations(session)

        elif menu_choice == 1:  # "Show Data" selected
            display_hierarchical_view(session)

        elif menu_choice == 2:  # "Import/Export" selected
            handle_import_export(session)

        elif menu_choice == 3:  # "Exit" selected
            break
