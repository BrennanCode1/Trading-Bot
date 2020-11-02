from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
from apikey import api_key
import pandas as pd
import json 
import requests
import time



i=0
lastPrice=0
for count in range (5):
    cc = ForeignExchange(key=api_key)
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    currentPrice=float (data["5. Exchange Rate"])
    compare = currentPrice - lastPrice
    print(compare)
    lastPrice=currentPrice
    print(lastPrice)
    time.sleep (20)
    i +=1


