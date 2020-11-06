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
import json
import pprint

timeout1=time.time() + 60*.5
timeout2=time.time() + 60*60

bank=0
owned =0 
Bitcoin=0
TotalBitcoin=0
crypto = 0
bitcoinUSD=1
compare1=.01
login = r.login('USERNAME','PASSWORD')

class read_data(object):
  def __init__(self, jdata):
    self.__dict__ = json.loads(jdata)

def buyingPower():
    data=r.load_phoenix_account(info=None)
    return data

def bankAmount():
    data=r.profiles.load_account_profile(info=None)
    bank= float(data["buying_power"])
    return bank


def currentPriceApiCall():
    cc = ForeignExchange(key='apikey')
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    currentPrice=float (data["5. Exchange Rate"]) 
    return currentPrice


def buy():
    bank=bankAmount()
    ableToSpend= float(bank * .10)
    return ableToSpend,bank
    
    
def sell():
    amountParse=buyingPower()
    obj=json.dumps(amountParse)
    p = read_data(obj)
    bitcoinUSD=float(p.crypto["equity"]["amount"])
    r.order_sell_crypto_by_price('BTC',bitcoinUSD)
    bank=bankAmount()
    print ("Bank total after sell : ", bank)
    print ("Bitcoin sold for",bitcoinUSD)
    return bitcoinUSD

amountParse=buyingPower()
obj=json.dumps(amountParse)
p = read_data(obj)
bitcoinUSD=float(p.crypto["equity"]["amount"])

bank=bankAmount()

fiveMinPrice= currentPriceApiCall()
currentPrice= currentPriceApiCall()
compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice
buycount=0

print ("Starting Bank Value:",bank)
print ("Starting BitcoinUSD Value:",bitcoinUSD)

while True:
    if compare > .25:
        spend,bank=buy()
        if spend > .16:
            r.order_buy_crypto_by_price('BTC',spend)
            compare1=compare
            buycount+=1
            BitcoinUSD+=1
            print ("Bitcoin Bought USD amount", spend)
            print ("Amount of buys made",buycount)
                spend=0
            time.sleep(60)
            if bitcoinUSD > 0:
                currentPrice= currentPriceApiCall()
                compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice
    while bitcoinUSD > 0:
            if compare < -.5:
                sell()
                bitcoinUSD=0
                time.sleep(180)
            if compare > compare1+.1:
                sell()
                bitcoinUSD=0
                time.sleep(180)
            if time.time()>timeout1:
                currentPrice= currentPriceApiCall()
                compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice 
                timeout1=time.time() + 60*.05
    if time.time()>timeout1:
         currentPrice= currentPriceApiCall()
         compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice 
         timeout1=time.time() + 60*.1
    if time.time()>timeout2:
        fiveMinPrice=currentPriceApiCall()
        print ("Thirtymin has been updated Outside of While Function")
        timeout2=time.time() + 60*60 
    
