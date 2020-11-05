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
login = r.login('USERNAME','PASSWORD')

def buyingPower():
    data=r.load_phoenix_account(info=None)
    return data

data=buyingPower()


obj=json.dumps(data)
# Declare class to store JSON data into a python dictionary
class read_data(object):
  def __init__(self, jdata):
    self.__dict__ = json.loads(jdata)


p = read_data(obj)
amount=p.crypto["equity"]["amount"]


