import rsdLibrary as lib
import exportPDF as epdf

import pandas as pd
from termcolor import colored
from simple_term_menu import TerminalMenu
import os

def RandomizeShop(df: pd.DataFrame, rgMod = 1):
	for index, row in df.iterrows():
		min = lib.ConvertValue(row['Minimum Value'])
		max = lib.ConvertValue(row['Maximum Value'])
		mean = round(min + ((max - min) / 2)) * rgMod
		if mean > max:
			mean = max
		if mean < min:
			mean = min

		X = lib.get_truncated_normal(mean = int(mean), low = min, upp = max)
		itemValue = round(X.rvs())
		lib.GetCoinPiece(itemValue)
		df.loc[[index], 'Current Value'] = lib.GetCoinPiece(itemValue)

def AddWealthIndicator(df: pd.DataFrame, path):
	RegionWealth = int(input("Specify Region wealth (1 - 10)\n 1 being extremely poor, 10 being extremely wealthy: "))
	if RegionWealth not in range(1, 11):
		exit(1)
	rgMod = round(lib.LinearConversion(RegionWealth, 10, 0, 0.5, 1.5), 1)
	df['Region Wealth'] = rgMod
	df.to_csv(path)
	print(colored("Added wealth indicator of: " + RegionWealth, 'green'))
	return RegionWealth

def AddItem(df: pd.DataFrame, path):
	add = []
	print(colored("Please enter the following info:", 'magenta'))
	while True:
		itemName = input("Item name:\n")
		if itemName in df['Item Name']:
			print(colored("Item already exists, please choose another", 'red'))
			continue
		break
	add.append(itemName)

	while True:
		print(colored("The next values are prices in cp, sp, gp or pp. Value and denomination seperated by a space", 'magenta'))
		minValue = input("Minimum value:\n")
		maxValue = input("Maximum value:\n")

		if ' ' not in minValue or ' ' not in maxValue:
			print(colored("Please enter a space between the value and the denomination", 'red'))
			continue
		minValueX = lib.ConvertValue(minValue)
		maxValueX = lib.ConvertValue(maxValue)
		if lib.ConvertValue(maxValue) < 1 or lib.ConvertValue(minValue) < 1:
			print(colored("Maximum and minimum values need to be higher than 1 cp", 'red'))
		if lib.ConvertValue(maxValue) - lib.ConvertValue(minValue) < 1:
			print(colored("Maximum value needs to be higher than the minimum value", 'red'))
			continue
		break
	add.append(lib.GetCoinPiece(round(minValueX + (maxValueX - minValueX) / 2)))
	add.append(minValue)
	add.append(maxValue)

	itemType = input("Item type:\n")
	add.append(itemType)
	add.append(1)
	df.loc[len(df)] = add
	df['Item Type'].sort_values()
	df.to_csv(path)
	print(colored("Added " + itemName + " to shop", 'green'))

def ExistingShop():
	print(colored("Select one of the following stored shops:", "magenta"))
	terminal_menu = TerminalMenu(lib.ReadCsv())
	terminal_menu.show()
	path = terminal_menu.chosen_menu_entry
	df = lib.read(path)

	x = 0
	while x != 1:
		modAddAnswer = ["Add item to shop", "Just randomize the shop data", "Randomize according to a wealth indicator", "Show shop data", "Return"]
		print(colored("Do you want to randomize shop data according to a wealth indicator?", "magenta"))
		terminal_menu = TerminalMenu(modAddAnswer)
		terminal_menu.show()
		if terminal_menu.chosen_menu_entry == "Add item to shop":
			AddItem(df, path)
		if terminal_menu.chosen_menu_entry == "Randomize according to a wealth indicator":
			if df['Region Wealth'][2] == 0:
				print(colored("Please first add a wealth indicator", "magenta"))
				rgMod = AddWealthIndicator(df, path)
				RandomizeShop(df, rgMod)
				return

			print("Would you like to modify the wealth indicator?")
			terminal_menu = TerminalMenu(["Yes", "No"])
			terminal_menu.show()
			if terminal_menu.chosen_menu_entry == "Yes":
				rgMod = AddWealthIndicator(df, path)
			rgMod = int(df.loc[2]['Region Wealth'])
			RandomizeShop(df, rgMod)

		if terminal_menu.chosen_menu_entry == "Just randomize the shop data":
			RandomizeShop(df, 1)

		if terminal_menu.chosen_menu_entry == "Show shop data":
			print(df)

		if terminal_menu.chosen_menu_entry == "Return":
			x = 1

def MakeNewShop():
	
	files = lib.ReadCsv()
	files = [temp.replace('.csv', '') for temp in files]
	files = [temp.replace('data/', '') for temp in files]

	while True:
		shopName = input(colored("Please specify shop name: \n", 'magenta'))
		if shopName in files:
			print(colored("Name already exists, please choose another", 'red'))
			continue
		shopName = "data/" + shopName + ".csv"
		print(shopName)
		break
		
	df = pd.DataFrame()
	df.insert(loc=0, column="Item Name", value="")
	df.insert(loc=1, column="Current Value", value="")
	df.insert(loc=2, column="Minimum Value", value="")
	df.insert(loc=3, column="Maximum Value", value="")
	df.insert(loc=4, column="Item Type", value="")
	df.insert(loc=5, column="Region Wealth", value="")
	open(shopName, mode='x')
	df.to_csv(shopName)
 
def ImportShop():
	importFiles = lib.ReadCsv("import/")
	if not importFiles:
		print(colored("No shops found for import", 'red'))
		return

	importFiles = [temp.replace('.csv', '') for temp in importFiles]
	importFiles = [temp.replace('import/', '') for temp in importFiles]
	print(colored("What shop would you like to import?", 'magenta'))
	terminal_menu = TerminalMenu(importFiles)
	terminal_menu.show()

	dataFiles = lib.ReadCsv("data/")
	if dataFiles:
		dataFiles = [temp.replace('.csv', '') for temp in dataFiles]
		dataFiles = [temp.replace('data/', '') for temp in dataFiles]
	if terminal_menu.chosen_menu_entry in dataFiles:
		print(colored("Shop already exists, please change the name of the file", 'red'))
		return

	df = lib.read("import/" + terminal_menu.chosen_menu_entry + ".csv")
	col = list(df.columns)
	colNames = ["Item Name", "Current Value", "Maximum Value", "Item Type", "Region Wealth"]
	if not all(value in col for value in colNames):
		print(colored("Could not find all needed collumns", 'red'))
		return

	open("data/" + terminal_menu.chosen_menu_entry + ".csv", mode='x')
	df['Item Type'].sort_values()
	df.to_csv("data/" + terminal_menu.chosen_menu_entry + ".csv")
	os.remove("import/" + terminal_menu.chosen_menu_entry + ".csv")
	print(colored("Succesfully added " + terminal_menu.chosen_menu_entry + " to program", 'green'))

def RemoveShop():
	print("Which store would you like to delete?")
	paths = lib.ReadCsv()
	terminal_menu = TerminalMenu(paths)
	terminal_menu.show()
	index = terminal_menu.chosen_menu_index

	print(colored("Are you sure you want to delete this shop?", "red", attrs=['bold']))
	print(colored("Doing so will permanently remove all data of this store", "red", attrs=['bold']))
	print(colored(terminal_menu.chosen_menu_entry, "green"))
	terminal_menu = TerminalMenu(["Yes", "No"])
	terminal_menu.show()
	if terminal_menu.chosen_menu_entry == "Yes":
		os.remove(paths[index])
	if terminal_menu.chosen_menu_entry == "No":
		return

def rsd():
	if not os.path.exists("data"):
		os.mkdir("data")
	if not os.path.exists("import"):
		os.mkdir("import")

	print(colored("Welcome to RandomShopData for TRGP!", "green", attrs=["bold"]))
	options = ["Choose existing shop", "Make new shop", "Import shop", "Remove shop", "Export to PDF", "Exit program"]
	terminal_menu = TerminalMenu(options)

	while True:
		print(colored("What would you like to do?", "green"))
		terminal_menu.show()
		if terminal_menu.chosen_menu_entry == "Choose existing shop":
			ExistingShop()
			continue
		if terminal_menu.chosen_menu_entry == "Make new shop":
			MakeNewShop()
			continue
		if terminal_menu.chosen_menu_entry == "Import shop":
			ImportShop()
			continue
		if terminal_menu.chosen_menu_entry == "Remove shop":
			RemoveShop()
			continue
		if terminal_menu.chosen_menu_entry == "Export to PDF":
			epdf.Export()
			continue
		if terminal_menu.chosen_menu_entry == "Exit program":
			break
