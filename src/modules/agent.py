"""

"""
import redis
import json
import abc


class Agent:
    """
    Main class for all agent type. Can publish on a redis channel.
    For subscriber, surcharge run method with while true.
    """

    def __init__(
            self,
            redis_publish_channel_name: str,
            redis_subscribe_channel_name: str,
            host='localhost',
            port=6379,
            *args
    ):
        """
        Create redis client and save current redis channels name.

        :param redis_publish_channel_name: The redis channel name where publish.
        :param redis_subscribe_channel_name: The redis channel name where subscribe.
        :param host: The host ip of redis client, default 'localhost'.
        :param port: The host port of redis client, default 6379.
        """
        self.redis_client = redis.Redis(host=host, port=port, decode_responses=True)
        self.redis_publish_channel_name = redis_publish_channel_name
        self.redis_subscribe_channel_name = redis_subscribe_channel_name

    @abc.abstractmethod
    def run(self):
        """
        Main method of an agent, contain the logic.
        """
        raise NotImplemented('This method need to be rewritten')

    def publish(self, message: dict):
        """
        Publish the given message in redis current channel.

        :param message: The message to publish
        """
        self.redis_client.publish(self.redis_publish_channel_name, json.dumps(message))
