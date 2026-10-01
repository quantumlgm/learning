import sys
from loguru import logger
import pika


RMQ_HOST = "127.0.0.1"
RMQ_PORT = 5672

MQ_EXCHANGE = ""
FANOUT_EXCHANGE = "new_post_events"
DIRECT_EXCHANGE = "logs_direct"
TOPIC_EXCHANGE = "shop_topic"

MQ_ROUTING_KEY = "news"

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    # credentials=pika.PlainCredentials()
)


def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)


logger.remove()


LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)


logger.add(
    sys.stdout,
    format=LOG_FORMAT,
    level="INFO",
    colorize=True,
    backtrace=False,
    diagnose=False,
)
