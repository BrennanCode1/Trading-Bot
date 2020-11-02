from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
from apikey import api_key
import threading 
import pandas as pd
import json 
import requests
import time


def currentPriceApiCall():
    for i in range (5):
        threading.Timer(20.0, currentPriceApiCall).start()
        cc = ForeignExchange(key=api_key)
        data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
        currentPrice=float (data["5. Exchange Rate"])
        i+=1
        print ("Current: " , currentPrice)
    return currentPrice

def fiveMinPriceApiCall():
    for i2 in range (1):
        threading.Timer(100.0, fiveMinPriceApiCall).start()
        cc = ForeignExchange(key=api_key)
        data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
        fiveMinPrice=float (data["5. Exchange Rate"])
        print ("Five: " , fiveMinPrice)
        i2+=1
    return fiveMinPrice    

i2=0
i=0
lastPrice=1

currentPriceApiCall()
fiveMinPriceApiCall()

currentPrice=currentPriceApiCall()
compare = (lastPrice / currentPrice) * 100 
print("compare",compare)
lastPrice=currentPrice
print("lastprice",lastPrice)




