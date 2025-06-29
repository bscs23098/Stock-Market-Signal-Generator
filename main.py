import dataCollect as dc
import indicatorCalculator as ic
import dataVisualizer as dv
import signalGenerator as sg

# dc.download_data()
data = dc.readFile("aapl_data.csv")
# print(data)
# dv.visualizeData(data)
indicatorData = ic.calculate_indicators(data)
# dv.visualizeIndicators(indicatorData)
signals = sg.generate_signals(indicatorData)
if signals is not None:
    print(signals.head())
else:
    print("No signals generated. Please check the data and indicators.")
