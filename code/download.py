import numpy as np
import pandas as pd
import pandas_datareader as pdr
import datetime 

sample_size = 10

nyse_tickers = pd.read_csv('data/companylist_nyse.csv', encoding='latin1')
nyse_tickers = nyse_tickers.loc[nyse_tickers.MarketCap != 0, ]

nasdaq_tickers = pd.read_csv('data/companylist_nasdaq.csv', encoding='latin1')
nasdaq_tickers = nasdaq_tickers.loc[nasdaq_tickers.MarketCap != 0, ]

sample1 = nyse_tickers.sample(sample_size)['Symbol'].tolist()
sample2 = nasdaq_tickers.sample(sample_size)['Symbol'].tolist()

sample = sample1 + sample2

for ticker in sample:
	df = pdr.get_data_yahoo(ticker,
		start=datetime.datetime(2010, 1, 1),
		end=datetime.datetime(2018, 7, 16))
	df.to_csv('data/stocks/' + ticker + '.csv')