import pandas as pd
from binance.client import Client
from func import Prices

client = Client()
crypto = 'BTCEUR'

candles = client.get_historical_klines(
  symbol = crypto,
  interval = Client.KLINE_INTERVAL_1MINUTE,
  start_str = 1612828800000,
  end_str = 1655852400000
)

prices = Prices(candles)

prices.to_csv(r'BTCEUR.csv', index=False, sep=';')
