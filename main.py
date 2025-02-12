import os
import time
import asyncio
import websockets

import pandas as pd

import json

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')


async def binance_ws():
    """
    Get trade information of a symbol at each transaction. The url is the stream of the executed transaction.
    For more information about streams, visit https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams
    """
    kline_stream = "wss://fstream.binance.com/ws/btcusdt@kline_1m"

    async with websockets.connect(kline_stream) as ws:
        while True:
            data = await ws.recv()
            data = json.loads(data)
            print(data)


if __name__ == "__main__":
    asyncio.run(binance_ws())


