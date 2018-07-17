import numpy as np
import pandas as pd
import pandas_datareader as pdr
import datetime 

nyse_tickers = pd.read_csv('data/companylist_nyse.csv', encoding='latin1')
nyse_tickers = nyse_tickers.loc[nyse_tickers.MarketCap != 0, ]

nasdaq_tickers = pd.read_csv('data/companylist_nasdaq.csv', encoding='latin1')
nasdaq_tickers = nasdaq_tickers.loc[nasdaq_tickers.MarketCap != 0, ]

list1 = nyse_tickers['Symbol'].str.strip().tolist()
list2 = nasdaq_tickers['Symbol'].str.strip().tolist()

tickers = list1 + list2

for ticker in tickers:
	df = pdr.get_data_yahoo(ticker,
		start=datetime.datetime(1950, 1, 1),
		end=datetime.datetime(2018, 7, 16))
	df.to_csv('data/stocks/' + ticker + '.csv')