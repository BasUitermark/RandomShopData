import pandas as pd
import glob
from scipy.stats import truncnorm

def read(path):
	df = pd.read_csv(path)
	return df

def LinearConversion(OldValue, OldMax, OldMin, NewMax, NewMin):
    return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def ReadCsv(path= "data/"):
	entries = []
	for file in glob.glob(path + "*.csv"):
		entries.append(file)
	return entries

def ConvertValue(value: str):
	convert = 0
	if 'cp' in value:
		convert = int(value[:-3])
	if 'sp' in value:
		convert = int(value[:-3]) * 10
	if 'ep' in value:
		convert = int(value[:-3]) * 50
	if 'gp' in value:
		convert = int(value[:-3]) * 100
	if 'pp' in value:
		convert = int(value[:-3]) * 1000
	return (convert)

def GetCoinPiece(coin):
	value = str()

	if coin < 10:
		value = str(coin) + ' cp'
	if coin < 100 and coin >= 10:
		coin = (coin // 10) + (coin % 10 > 5)
		value = str(int(coin)) + ' sp'
	if coin < 1000 and coin >= 100:
		coin = (coin // 100) + (coin % 100 > 5)
		value = str(int(coin)) + ' gp'
	if coin < 10000 and coin > 1000:
		coin = (coin // 100) + (coin % 100 > 5)
		value = str(int(coin)) + ' gp'
	if coin > 10000:
		coin = (coin // 1000)
		value = str(int(coin)) + ' pp'
	return value