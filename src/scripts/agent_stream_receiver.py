import websockets
import json
import logging

from abc import ABC

from src.modules.agent import Agent

class AgentStreamReceiver(Agent, ABC):
    """
    Agent to listen stream and publish data into redis bus.
    """

    def __init__(
            self,
            redis_publish_channel_name: str,
            redis_subscribe_channel_name: str,
            stream: str,
            host='localhost',
            port=6379,
    ):
        """
        Create redis client and save current redis channels name.

        :param redis_publish_channel_name: The redis channel name where publish.
        :param redis_subscribe_channel_name: The redis channel name where subscribe.
        :param stream: The stream to listen.
        :param host: The host ip of redis client, default 'localhost'.
        :param port: The host port of redis client, default 6379.
        """
        super().__init__(redis_publish_channel_name, redis_subscribe_channel_name, host, port)
        self.stream = stream

    async def run(self):
        async with websockets.connect(self.stream) as ws:
            while True:
                data = await ws.recv()  # get market info in async mode
                market_data = json.loads(data)
                logging.info(market_data)
                self.publish(market_data)
