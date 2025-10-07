import requests
import pandas as pd

def get_stock_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extract the time series dictionary
        time_series = data["Time Series (5min)"]
        # Convert the nested dictionary into a DataFrame
        df = pd.DataFrame.from_dict(time_series, orient='index')
        # Clean up column names
        df.columns = ["Open", "High", "Low", "Close", "Volume"]
        # Convert index to datetime
        df.index = pd.to_datetime(df.index)
        # Sort in ascending order of time
        df = df.sort_index()
        return df
    else:
        print(f"Error {response.status_code}: Unable to fetch data")
        return None

df = get_stock_data()
print(df.head())
