import json
from loguru import logger
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties
from technologies.RabbitMQ.config import get_connection

QUEUE_NAME = "safe_queue"


def process_payment(
    ch: BlockingChannel,
    method: Basic.Deliver,
    properties: BasicProperties,
    body: bytes
):
    try:
        data = json.loads(body.decode("utf-8"))
        logger.info(f"Списали деньги по платежу #{data['payment_id']} на сумму {data['amount']} руб.")
        
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"Ошибка при обработке платежа: {e}")
        ch.basic_reject(delivery_tag=method.delivery_tag, requeue=False)


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            # Очередь должна быть объявлена как durable=True
            channel.queue_declare(queue=QUEUE_NAME, durable=True)
            channel.basic_qos(prefetch_count=1)

            channel.basic_consume(
                queue=QUEUE_NAME,
                on_message_callback=process_payment,
                auto_ack=False
            )
            logger.info("Воркер ожидает платежи...")
            channel.start_consuming()


if __name__ == "__main__":
    main()