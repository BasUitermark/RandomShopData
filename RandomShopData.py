import pandas as pd
from termcolor import colored
from simple_term_menu import TerminalMenu

def read(path):
	df = pd.read_csv(path)
	return df

def RandomShopData():
	print("Select one of the following data entries")
	#read through the data folder for sheets and display the names in term_menu

def MakeNewShop():
	userInput = input("Please specify shop name: ")
	
	

if __name__ == "__main__":
	print(colored("Welcome to RandomShopData for TRGP!\n", "green"), colored("What would you like to do?", "green"))
	options = ["Randomize prices for existing shop data", "Make new shop", "Add item to shop", "Change region wealth statistic"]
	terminal_menu = TerminalMenu(options)
	menu_entry_index = terminal_menu.show()
	if menu_entry_index == 0:
		RandomShopData()
	if menu_entry_index == 1:
		MakeNewShop()
	# if userInput is 1:
	# 	RandomShopData()
	# if userInput is 2:
	# 	MakeNewData()
	# RegionWealth = int(input("Specify city wealth (1 - 10): "))
	# if RegionWealth not in range(1, 10):
	# 	exit(1)
	# print("City wealth is: ", RegionWealth)
	# blacksmith_RawData = read('data/DnD Shop Price Data - Blacksmith.csv')