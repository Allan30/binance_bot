import json
import redis
import abc

class Receiver:
    """
    Main class of all receivers type. Use two functions :

    1. Listen a stream or other to fetch data.
    2. Send fetched data into current redis channel.
    """

    def __init__(self, redis_channel_name: str):
        """
        Create redis client and save current redis channel name.

        :param redis_channel_name: The redis channel name where to publish.
        """
        self.redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.redis_channel_name = redis_channel_name

    @abc.abstractmethod
    def run(self):
        """
        Loop where to listen and publish. With binance use async with websockets methods.
        """
        raise NotImplemented('This method need to be rewritten')

    @abc.abstractmethod
    def listen(self) -> dict:
        """
        Listen stream to fetch data.
        """
        raise NotImplemented('This method need to be rewritten')

    def publish(self, message: dict):
        """
        Publish the given message in redis current channel.

        :param message: The message to publish
        """
        self.redis_client.publish(self.redis_channel_name, json.dumps(message))