from API_requests import get_balance_sheet, get_overview, get_stock_info
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData

# Displaying the data from the API

def print_data(data):
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"\n{key}: {value}")
    elif isinstance(data, pd.DataFrame):
        print(data)


# Main
    
while True:
    userInput = input("""\nWelcome to the application. Please choose from the following options:

    1. View company overview
    2. Get daily stock info
    3. View a balance sheet
    4. Close the application
          
    Select by entering a number followed by the enter key:\n    
          """)
    
    if userInput == '1':
        symbol = input("Select a stock by typing its ticker symbol followed by the enter key: ")
        overview_data = get_overview(symbol)
        print_data(overview_data)

    elif userInput == '2':
        symbol = input("Select a stock by typing its ticker symbol followed by the enter key: ")
        latest_stock_info = get_stock_info(symbol)
        print_data(latest_stock_info)

    elif userInput == "3":
        symbol = input("Select a stock by typing its ticker symbol followed by the enter key: ")
        balance_sheet = get_balance_sheet(symbol)
        print_data(balance_sheet)

    elif userInput == '4':
         print("\nClosing application...")
         break

    else:
        print("\nInvalid input. Try again.")

        



