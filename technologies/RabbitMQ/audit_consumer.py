import json
from loguru import logger
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from technologies.RabbitMQ.config import TOPIC_EXCHANGE, get_connection


QUEUE_NAME = "order_audit_queue"


def process_audit(
    ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes
):
    data = json.loads(body.decode("utf-8"))
    logger.success(f"[AUDIT SERVICE] Новая запись: {method.routing_key} | {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            channel.exchange_declare(exchange=TOPIC_EXCHANGE, exchange_type="topic")
            channel.queue_declare(queue=QUEUE_NAME)
            
            channel.queue_bind(
                exchange=TOPIC_EXCHANGE,
                queue=QUEUE_NAME,
                routing_key="*.created"
            )

            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(
                queue=QUEUE_NAME,
                on_message_callback=process_audit,
                auto_ack=False
            )
            logger.info(f"Слушаем события '*.created' в '{QUEUE_NAME}'...")
            channel.start_consuming()


if __name__ == "__main__":
    main()