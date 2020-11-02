from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
from apikey import api_key
import pandas as pd
import json 
import requests
import time


#ts = TimeSeries(key=api_key, output_format='pandas')
#data, meta_data = ts.get_quote_endpoint(symbol='AAPL')


#for label, row in data.iterrows():
#    print(row["05. price"])
i=0
for count in range (5):
    cc = ForeignExchange(key=api_key)
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    currentPrice=data["5. Exchange Rate"]
    print(currentPrice)
    time.sleep (20)
    i +=1


