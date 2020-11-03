from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
from apikey import api_key
from multiprocessing import Process
from threading import Timer
import sys
import pandas as pd
import json 
import requests
import time
timeout=time.time() + 60*1

i2=0
i=0 
lastPrice = 1

def currentPriceApiCall():
    cc = ForeignExchange(key=api_key)
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    currentPrice=float (data["5. Exchange Rate"]) 
    return currentPrice

def fiveMinPriceApiCall():
    cc = ForeignExchange(key=api_key)
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    fiveMinPrice=float (data["5. Exchange Rate"])
    print("Completed")
    return fiveMinPrice
       

def calculate():
    fiveMinPrice=fiveMinPriceApiCall()
    while True:
        currentPrice= currentPriceApiCall()
        compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice  
        print("current",currentPrice)
        print("compare",compare)
        print("fivemin",fiveMinPrice)
        time.sleep(20)
        if time.time()>timeout:
            fiveMinPrice=fiveMinPriceApiCall()



calculate()
#if __name__=='__main__':
    #p1 = Process(target=calculate)
    #p1.start()
    #p2 = Process(target=fiveMinPriceApiCall)
    #p2.start()
    #p1.join()
    #p2.join()


