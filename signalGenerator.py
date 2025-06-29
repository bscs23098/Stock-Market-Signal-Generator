import pandas as pd
import numpy as np
from indicatorCalculator import calculate_indicators
def generate_signals(df):
    if df is None or df.empty:
        print("DataFrame is empty or None. Cannot generate signals.")
        return None
    try:
        # Ensure 'Close' is numeric
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df.dropna(subset=['Close'], inplace=True)
        # Calculate indicators if not already present
        if 'SMA_20' not in df.columns or 'RSI_14' not in df.columns or 'BB_Upper' not in df.columns or 'BB_Lower' not in df.columns:
            df = calculate_indicators(df)
        signals = pd.DataFrame(index=df.index)
        signals['Buy_Signal'] = np.where((df['Close'] > df['SMA_20']) & (df['RSI_14'] < 30), 1, 0)
        signals['Sell_Signal'] = np.where((df['Close'] < df['SMA_20']) & (df['RSI_14'] > 70), -1, 0)
        signals['Bollinger_Buy'] = np.where(df['Close'] < df['BB_Lower'], 1, 0)
        signals['Bollinger_Sell'] = np.where(df['Close'] > df['BB_Upper'], -1, 0)
        signals['Signal'] = signals['Buy_Signal'] + signals['Sell_Signal'] + signals['Bollinger_Buy'] + signals['Bollinger_Sell']
        signals.drop(columns=['Buy_Signal', 'Sell_Signal', 'Bollinger_Buy', 'Bollinger_Sell'], inplace=True)
        return signals
    except KeyError as e:
        print(f"Missing column in DataFrame: {e}")
        return None