import json
import time
from fastapi import routing
from loguru import logger
from pika import data
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from technologies.RabbitMQ.config import DIRECT_EXCHANGE, TOPIC_EXCHANGE, get_connection


QUEUE_NAME = "payments_monitoring_queue"


def process_payment(
    ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes
):
    data = json.loads(body.decode("utf-8"))
    logger.warning(f"[PAYMENTS SERVICE] Ключ: {method.routing_key} | Данные: {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            channel.exchange_declare(
                exchange=TOPIC_EXCHANGE,
                exchange_type="topic"
            )
            channel.queue_declare(queue=QUEUE_NAME)

            channel.queue_bind(
                exchange=TOPIC_EXCHANGE,
                queue=QUEUE_NAME,
                routing_key="payments.#"
            )
            channel.basic_qos(prefetch_count=1)

            channel.basic_consume(
                queue=QUEUE_NAME,
                on_message_callback=process_payment,
                auto_ack=False,
            )
            logger.info(f"[PAYMENTS] Слушаем платежи '{QUEUE_NAME}'...")
            channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("[ERROR] Воркер остановлен.")