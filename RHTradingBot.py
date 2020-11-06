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

#Start Amount of time before refresshing api call   
timeout1=time.time() + 60*.5
timeout2=time.time() + 60*60
#Calling Variables in global before use
bank=0
owned =0 
Bitcoin=0
TotalBitcoin=0
crypto = 0
bitcoinUSD=1
compare1=.01
login = r.login('','')

#Reading the API call data from RH
class read_data(object):
  def __init__(self, jdata):
    self.__dict__ = json.loads(jdata)
#Loading how much BTC i have
def buyingPower():
    data=r.load_phoenix_account(info=None)
    return data
#Loading amount of money to spend
def bankAmount():
    data=r.profiles.load_account_profile(info=None)
    bank= float(data["buying_power"])
    return bank

#Current price of BTC
def currentPriceApiCall():
    cc = ForeignExchange(key='')
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    currentPrice=float (data["5. Exchange Rate"]) 
    return currentPrice

#getting 10% of Bank Account
def buy():
    bank=bankAmount()
    ableToSpend= float(bank * .10)
    return ableToSpend,bank
    
#Selling all BTC ammounts    
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
#Calling data needed, how much btc I have

amountParse=buyingPower()
obj=json.dumps(amountParse)
p = read_data(obj)
bitcoinUSD=float(p.crypto["equity"]["amount"])
#Bank information

bank=bankAmount()
#Getting the first api call of each price to compare
fiveMinPrice= currentPriceApiCall()
currentPrice= currentPriceApiCall()
#Formula to find out the percent change over the hour
compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice
buycount=0

print ("Starting Bank Value:",bank)
print ("Starting BitcoinUSD Value:",bitcoinUSD)
#Algo
while True:
    if compare > .2:
    #getting variables from buy to use in spend
        spend,bank=buy()
        if spend > .16:
            #buying the crypto with 10% of bank acc
            r.order_buy_crypto_by_price('BTC',spend)
            compare1=compare
            buycount+=1
            bitcoinUSD+=1
            print ("Bitcoin Bought USD amount", spend)
            print ("Amount of buys made",buycount)
            spend=0
            #updating the call
            if bitcoinUSD > 0:
                currentPrice= currentPriceApiCall()
                compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice
    while bitcoinUSD > 0:
        #looping here while bitcoin more thna 0 to only do one trade at a time
            if compare < -1
                sell()
                bitcoinUSD=0
                time.sleep(180)
            if compare > compare1+.60:
                sell()
                bitcoinUSD=0
                time.sleep(180)
            if time.time()>timeout1:
                currentPrice= currentPriceApiCall()
                compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice 
                timeout1=time.time() + 60*.05
    #refreshing apiu calls in allotated time
    if time.time()>timeout1:
         currentPrice= currentPriceApiCall()
         compare = 100 * (currentPrice - fiveMinPrice) / fiveMinPrice 
         timeout1=time.time() + 60*.1
    if time.time()>timeout2:
        fiveMinPrice=currentPriceApiCall()
        print ("Thirtymin has been updated Outside of While Function")
        timeout2=time.time() + 60*60 
    
