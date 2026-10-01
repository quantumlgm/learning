


import json
from pika.adapters.blocking_connection import BlockingChannel
from pika import BasicProperties
from pika.spec import Basic

from technologies.RabbitMQ.config import FANOUT_EXCHANGE, get_connection, logger


QUEUE_NAME = "telegram_notifications"


def process_telegram(
    ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes
):    
    data = json.loads(body.decode("utf-8"))    
    logger.success(f"[TELEGRAM] Отправляем сообщение подписчикам о посте: '{data['title']}'")
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
                on_message_callback=process_telegram,
                auto_ack=False,
            )
            logger.info(f"[TELEGRAM] Слушаем очередь '{QUEUE_NAME}'...")
            channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("[TELEGRAM] Воркер остановлен.")