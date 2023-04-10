import pandas as pd

def read(path):
	df = pd.read_csv(path)
	return df

if __name__ == "__main__":
	blacksmith_RawData = read('data/DnD Shop Price Data - Blacksmith.csv')
	print(blacksmith_RawData)