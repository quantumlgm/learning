import json
import time
from loguru import logger
from pika import data
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from technologies.RabbitMQ.config import FANOUT_EXCHANGE, MQ_ROUTING_KEY, get_connection


QUEUE_NAME = "email_notifications"


def process_email(
    ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes
):    
    data = json.loads(body.decode("utf-8"))    
    logger.success(f"[EMAIL] Отправляем письмо подписчикам о посте: '{data['title']}'")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            channel.exchange_declare(
                exchange=FANOUT_EXCHANGE,
                exchange_type="fanout"
            )
            channel.queue_declare(queue=QUEUE_NAME)

            channel.queue_bind(
                queue=QUEUE_NAME,
                exchange=FANOUT_EXCHANGE,                
            )
            channel.basic_qos(prefetch_count=1)

            channel.basic_consume(
                queue=QUEUE_NAME,
                on_message_callback=process_email,
                auto_ack=False,
            )
            logger.info(f"[EMAIL] Слушаем очередь '{QUEUE_NAME}'...")
            channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("[EMAIL] Воркер остановлен.")