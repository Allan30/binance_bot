import os
import websockets
import json

from binance.client import Client
from dotenv import load_dotenv

from src.scripts.trade_analyzer import Analyzer
from src.scripts.trade_executor import TradeExecutor

class TradeScheduler:

    def __init__(self):
        self.kline_stream = "wss://fstream.binance.com/ws/btcusdt@kline_1m"
        self.analyzer = Analyzer()
        self.executor = TradeExecutor()

    async def run(self):
        """
        Get trade information of a symbol at each transaction. The url is the stream of the executed transaction.
        For more information about streams, visit https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams
        """
        load_dotenv()
        binance_client = Client(os.getenv('API_KEY'), os.getenv('API_SECRET'), testnet=True)
        async with websockets.connect(self.kline_stream) as ws:
            while True:
                market_data = await ws.recv() #get market info in async mode
                market_data = json.loads(market_data)

                account_info = binance_client.futures_account() #info of the futures mock binance account

                for balance in account_info['assets']:
                    if balance['asset'] == 'BTC':  # find BTC
                        available_balance = balance['availableBalance']
                        print(f"Solde BTC disponible : {available_balance}")
                        unrealized_profit = balance['unrealizedProfit']
                        print(f"Profit non réalisé : {unrealized_profit}")
                        break

                print(market_data)  # TODO Give this data to the analyzer, depending of the result use executor to
                                    # perform operation