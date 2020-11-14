ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for data in ohlc[1:]:
    if data[ohlc[0].index("close")] >= data[ohlc[0].index("open")]:
        print(data[ohlc[0].index("close")])
