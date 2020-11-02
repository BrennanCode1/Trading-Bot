from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
from apikey import api_key
import pandas as pd
import json 
import requests



#ts = TimeSeries(key=api_key, output_format='pandas')
#data, meta_data = ts.get_quote_endpoint(symbol='AAPL')


#for label, row in data.iterrows():
#    print(row["05. price"])
    



cc = ForeignExchange(key=api_key)
data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')


for label, row in data.items():
    print(data["5. Exchange Rate"])