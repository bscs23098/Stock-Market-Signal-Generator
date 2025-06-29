import yfinance as yf
import numpy as np
import pandas as pd

def download_data():
    data = yf.download("AAPL", start="2022-01-01", end="2023-01-01")
    data.to_csv("aapl_data.csv")

def readFile(filename="aapl_data.csv"):
    try:
        df = pd.read_csv(filename)

        # Drop rows where the date column is not valid
        df.rename(columns={df.columns[0]: "Date"}, inplace=True)
        df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d", errors="coerce")
        df.dropna(subset=["Date"], inplace=True)

        # Set the valid parsed date as index
        df.set_index("Date", inplace=True)

        # Drop any remaining rows with missing essential data
        df.dropna(inplace=True)

        return df

    except FileNotFoundError:
        print(f"File {filename} not found. Please download the data first.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

