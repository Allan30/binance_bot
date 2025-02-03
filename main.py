import os

from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

client = Client(api_key, api_secret)

print(client.get_account())
print(client.get_symbol_ticker(symbol="BTCUSDT"))