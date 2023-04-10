import pandas as pd

def read(path):
	df = pd.read_csv(path)
	return df

if __name__ == "__main__":
	RegionWealth = int(input("Specify city wealth (1 - 10): "))
	if RegionWealth not in range(1, 10):
		exit(1)
	print("City wealth is: ", RegionWealth)
	blacksmith_RawData = read('data/DnD Shop Price Data - Blacksmith.csv')