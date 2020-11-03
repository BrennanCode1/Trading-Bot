from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
from apikey import api_key
from multiprocessing import Process
from threading import Timer
import time
import datetime
import sys
import pandas as pd
import json 
import requests

timeout=time.time() + 60*5
timeout1=time.time() + 60*.3
timeout2=time.time() + 60*2
 
bank = 500
owned =0 
Bitcoin=0

def currentPriceApiCall():
    cc = ForeignExchange(key=api_key)
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    currentPrice=float (data["5. Exchange Rate"]) 
    return currentPrice

def fiveMinPriceApiCall():
    cc = ForeignExchange(key=api_key)
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    fiveMinPrice=float (data["5. Exchange Rate"])
    return fiveMinPrice
       

#def calculate():
#    global fiveMinPrice
#    currentPrice= currentPriceApiCall()
#    compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice 
#    if time.time()>timeout:
#        fiveMinPrice=fiveMinPriceApiCall()
#        print ("Ran 5 minute")
#    return compare,currentPrice
    

def buy():
    global bank
    ableToSpend= bank * .10
    bank = bank -ableToSpend
    print ("Bank total after buy: ", bank)
    return ableToSpend,bank
    
    
def sell():
    currentPrice = currentPriceApiCall()
    global bank, Bitcoin
    owned = Bitcoin * currentPrice
    bank = owned+ bank
    print ("Bank total after sell : ", bank)
    return bank



fiveMinPrice= currentPriceApiCall()
currentPrice= currentPriceApiCall()
compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice
print (compare)
while True:
    if compare > .1:
        spend,bank=buy()
        Bitcoin= spend / currentPrice
        print ("Bitcoin amount",Bitcoin)
        print (bank)
    if compare < -.1:
        sell()
        print ("Bitcoin sold",Bitcoin)
    if compare > .15:
        sell()
        print("Bitcoin sold: ",Bitcoin)
    if time.time()>timeout1:
         currentPrice= currentPriceApiCall()
         compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice 
         print ("Compare and Current Price updated")
         print ("Compare: " ,compare)
    if time.time()>timeout2:
        fiveMinPrice=fiveMinPriceApiCall()
        print ("FiveminPrice has been updated")
        timeout2=time.time() + 60*2
    time.sleep(20)

        





    


