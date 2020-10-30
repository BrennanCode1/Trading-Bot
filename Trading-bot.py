from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from pprint import pprint
import asyncio
from alpha_vantage.async_support.timeseries import TimeSeries
import os
import requests
from apikey import api_key
#cc = ForeignExchange(key=api_key)
#data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
#pprint(data)


ts = TimeSeries(key=api_key)
data, meta_data = ts.get_quote_endpoint('GOOGL')

pprint(data)

