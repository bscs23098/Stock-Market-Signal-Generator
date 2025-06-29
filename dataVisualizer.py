import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

def visualizeData(data):
    if data is None or data.empty:
        print("No data to visualize.")
        return

    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')

    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)

    # Format x-axis
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)

    # ✅ Improve Y-axis: force clean numeric ticks
    ax = plt.gca()
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))  # Reduce y-axis ticks
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"${x:,.2f}"))  # Format as currency

    plt.tight_layout()
    plt.show()

def visualizeIndicators(data):
    if data is None or data.empty:
        print("No data to visualize.")
        return
    plt.figure(figsize=(14, 10))
    plt.subplot(2, 1, 1)
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    plt.plot(data.index, data['SMA_20'], label='SMA 20', color='orange')
    plt.plot(data.index, data['SMA_50'], label='SMA 50', color='green')
    plt.plot(data.index, data['EMA_20'], label='EMA 20', color='red')
    plt.plot(data.index, data['EMA_50'], label='EMA 50', color='purple')
    plt.fill_between(data.index, data['BB_Upper'], data['BB_Lower'], color='lightgray', alpha=0.5, label='Bollinger Bands')
    plt.title('Stock Price with Indicators')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    plt.subplot(2, 1, 2)
    plt.plot(data.index, data['RSI_14'], label='RSI 14', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.show()