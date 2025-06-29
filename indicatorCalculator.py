import pandas as pd
import numpy as np

def calculate_indicators(df):
    if df is None or df.empty:
        print("DataFrame is empty or None. Cannot calculate indicators.")
        return None

    try:
        # Ensure 'Close' is numeric
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df.dropna(subset=['Close'], inplace=True)

        # Moving Averages
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
        df['EMA_50'] = df['Close'].ewm(span=50, adjust=False).mean()

        # Bollinger Bands (20-day)
        df['BB_Middle'] = df['SMA_20']
        df['BB_Std'] = df['Close'].rolling(window=20).std()
        df['BB_Upper'] = df['BB_Middle'] + 2 * df['BB_Std']
        df['BB_Lower'] = df['BB_Middle'] - 2 * df['BB_Std']

        # RSI (14-day)
        delta = df['Close'].diff()
        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)

        avg_gain = pd.Series(gain, index=df.index).rolling(window=14).mean()
        avg_loss = pd.Series(loss, index=df.index).rolling(window=14).mean()

        rs = avg_gain / (avg_loss + 1e-10)  # avoid division by zero
        df['RSI_14'] = 100 - (100 / (1 + rs))

        return df

    except KeyError as e:
        print(f"Missing column in DataFrame: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
