import sys
from loguru import logger
import pika


EXCHANGE = "order_exchange"


parameters = pika.ConnectionParameters(
    host="127.0.0.1", 
    port=5672,
)


def get_connection():
    return pika.BlockingConnection(
        parameters=parameters
    )


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
