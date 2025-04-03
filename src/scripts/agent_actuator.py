import json
import logging

from abc import ABC

from src.modules.agent import Agent

class AgentActuator(Agent, ABC):
    """
    Agent get analyze from analyzer agent and send action to binance.
    """

    def __init__(
            self,
            redis_publish_channel_name: str,
            redis_subscribe_channel_name: str,
            host='localhost',
            port=6379,
    ):
        """
        Create redis client and save current redis channels name.

        :param redis_publish_channel_name: The redis channel name where publish.
        :param redis_subscribe_channel_name: The redis channel name where subscribe.
        :param host: The host ip of redis client, default 'localhost'.
        :param port: The host port of redis client, default 6379.
        """
        super().__init__(redis_publish_channel_name, redis_subscribe_channel_name, host, port)
        self.pubsub = self.redis_client.pubsub()
        self.pubsub.subscribe(redis_subscribe_channel_name)

    def run(self):
        while True:
            for message in self.pubsub.listen():
                if message["type"] == "message":
                    logging.info(f"Message reçu: {json.loads(message['data'])}")
                    self.publish(message)