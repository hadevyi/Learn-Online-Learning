import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

max_price = float(btc['max_price'])
min_price = float(btc['min_price'])
gap = max_price - min_price
market_price = float(btc['opening_price'])
max_price = float(btc['max_price'])

if (market_price+gap) > max_price:
    print("상승장")
else:
    print("하락장")
