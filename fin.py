import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import date,datetime,time,timezone

def get_stock_data(ticker,start,end):
    data = yf.download(ticker, start=start, end=end,auto_adjust=False)
