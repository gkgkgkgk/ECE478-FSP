import pandas_datareader.data as web
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import scipy.optimize as optimize
from numpy import random
import yfinance as yfin

startdate= datetime(year=2017,month=12,day=31)
enddate= datetime(year=2018,month=12,day=31)
ticks=['AAPL', 'MSFT', 'GOOGL', 'META', 'NVDA', 'AMZN', 'TSLA', 'HD', 'TM', 'NKE']

data = {}

# pull data for each stock
for tick in ticks:
    data[tick] = web.DataReader(tick,'yahoo',startdate, enddate).drop(columns=['High', 'Low', 'Open', 'Close', 'Volume'])

