from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import pandas as pd

# Set API_KEY to the Alpha Vantage API key obtained from Alpha Vantage website (https://www.alphavantage.co)
API_KEY = 'insert key'

# Functions for requesting data from the Alpha Vantage API with data formatting

def get_overview(symbol):
    API_data = FundamentalData(key=API_KEY)
    overview_data, _ = API_data.get_company_overview(symbol)
    overview_df = pd.DataFrame([overview_data])
    overview_df = overview_df.T
    overview_df.columns = ['Stock Overview']
    return overview_df

def get_stock_info(symbol):
    API_data = TimeSeries(key=API_KEY)
    stock_data, _ = API_data.get_daily_adjusted(symbol)
    stock_df = pd.DataFrame.from_dict(stock_data).T
    stock_df.reset_index(level=0, inplace=True)
    stock_df = stock_df.rename(columns={'index': 'date'})
    stock_df.sort_values('date', inplace=True)
    latest_stock_info = stock_df.iloc[-1]
    latest_stock_info = pd.DataFrame(latest_stock_info).T
    latest_stock_info = latest_stock_info.T
    latest_stock_info.reset_index(inplace=True)
    latest_stock_info.columns = ['Data Type', 'Data']
    return latest_stock_info


def get_balance_sheet(symbol):
    API_data = FundamentalData(key=API_KEY)
    balance_sheet, _ = API_data.get_balance_sheet_quarterly(symbol)
    balance_sheet_df = pd.DataFrame.from_dict(balance_sheet).T
    balance_sheet_df.reset_index(level=0, inplace=True)
    balance_sheet_df = balance_sheet_df.rename(columns={'index': 'data'})
    return balance_sheet_df