from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
from apikey import api_key
from multiprocessing import Process
from threading import Timer
import robin_stocks.helper as helper
import robin_stocks.urls as urls
import robin_stocks as r
import time
import datetime
import sys
import pandas as pd
import json 
import requests

timeout1=time.time() + 60*.5
timeout2=time.time() + 60*30

bank=500
owned =0 
Bitcoin=0
TotalBitcoin=0

#login = r.login('USERNAME','PASSWORD')

def buyingPower():
    data=r.profiles.load_account_profile(info=None)
    bank= float(data["buying_power"])
    return bank


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
          

def buy():
    global bank
    ableToSpend= bank * .10
    bank = bank -ableToSpend
    print ("Bank total after buy: ", bank)
    return ableToSpend,bank
    
    
def sell():
    global bank , Bitcoin
    currentPrice = currentPriceApiCall()
    owned = TotalBitcoin * currentPrice
    bank = owned+ bank
    print ("Bank total after sell : ", bank)
    print ("Bitcoin sold",TotalBitcoin)
    return bank


 
#bank =buyingPower()
fiveMinPrice= currentPriceApiCall()
currentPrice= currentPriceApiCall()
compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice
buycount=0
while True:
    if compare > .1:
        spend,bank=buy()
        Bitcoin= spend / currentPrice
        print("Bitcoin Bought!")
        print ("Bitcoin amount",Bitcoin)
        compare1=compare
        time.sleep(60)
        buycount+=1
        print ("Amount of buys made",buycount)
        if Bitcoin > 0:
            TotalBitcoin = Bitcoin + TotalBitcoin
            currentPrice= currentPriceApiCall()
            compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice
    while TotalBitcoin > 0:
        if compare < -.1:
            sell()
            TotalBitcoin=0
        if compare > compare1+.1:
            sell()
            TotalBitcoin=0
        if time.time()>timeout1:
            currentPrice= currentPriceApiCall()
            compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice 
            print ("Compare and Current Price updated")
            print ("Total Bitcoin: ", TotalBitcoin)
            timeout1=time.time() + 60*.5
        if time.time()>timeout2:
            fiveMinPrice=fiveMinPriceApiCall()
            print ("Thirtymin has been updated")
            timeout2=time.time() + 60*30  
    if time.time()>timeout1:
         currentPrice= currentPriceApiCall()
         compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice 
         print ("Compare and Current Price updated")
         print ("Total Bitcoin: ", TotalBitcoin)
         timeout1=time.time() + 60*.5
    if time.time()>timeout2:
        fiveMinPrice=fiveMinPriceApiCall()
        print ("Thirtymin has been updated")
        timeout2=time.time() + 60*30      