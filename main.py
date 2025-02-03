import os

from binance.client import Client
from dotenv import load_dotenv
import time

import pandas as pd

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

client = Client(api_key, api_secret, testnet=True)

def get_futures_data(symbol, interval='1m', limit=100):
    klines = client.futures_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                       'close_time', 'quote_asset_volume', 'trades', 'taker_base_vol',
                                       'taker_quote_vol', 'ignore'])
    df['close'] = df['close'].astype(float)  # Convertir en float
    return df[['timestamp', 'close']]


def calculate_sma(df, short_window=10, long_window=50):
    df['SMA_10'] = df['close'].rolling(window=short_window).mean()
    df['SMA_50'] = df['close'].rolling(window=long_window).mean()
    return df


def check_signals(df):
    latest = df.iloc[-1]
    previous = df.iloc[-2]
    print(latest)
    print(previous)
    if previous['SMA_10'] < previous['SMA_50'] and latest['SMA_10'] > latest['SMA_50']:
        return "BUY"  # Achat (LONG)
    elif previous['SMA_10'] > previous['SMA_50'] and latest['SMA_10'] < latest['SMA_50']:
        return "SELL"  # Vente (SHORT)
    return None


def place_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        print(f"Ordre {side} exécuté avec succès !")
        return order
    except Exception as e:
        print(f"Erreur lors de l'exécution de l'ordre : {e}")


symbol = "BTCUSDT"
quantity = 0.001  # Quantité à trader

count=0
while True:
    print(count)
    df = get_futures_data(symbol)
    df = calculate_sma(df)

    signal = check_signals(df)

    if signal == "BUY":
        place_order(symbol, "BUY", quantity)  # Achat (LONG)
    elif signal == "SELL":
        place_order(symbol, "SELL", quantity)  # Vente (SHORT)
    print(signal)
    count += 1
    time.sleep(60)

