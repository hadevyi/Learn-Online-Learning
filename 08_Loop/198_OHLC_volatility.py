ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

volatility = []

for data in ohlc[1:]:
    volatility.append(data[ohlc[0].index("high")] - data[ohlc[0].index("low")])

print(volatility)
