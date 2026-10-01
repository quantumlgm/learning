import json
from loguru import logger
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from technologies.RabbitMQ.config import EXCHANGE, get_connection



def show_orders(
    ch: BlockingChannel, 
    method: Basic.Deliver,
    propeties: BasicProperties,
    body: bytes
):
    data = json.loads(body.decode("utf-8"))
    logger.success(f"[ANALYTIC] Обрабатываем заказ: '{data['order_id']}' с суммой '{data['cost']}'")
    ch.basic_ack(method.delivery_tag)


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            channel.exchange_declare(
                exchange=EXCHANGE,
                exchange_type="topic"                
            )
            channel.queue_declare(queue="analytic_queue", durable=True)
            channel.queue_bind(
                exchange=EXCHANGE,
                queue="analytic_queue",
                routing_key="*.msk.*.*"
            )
            channel.basic_qos(prefetch_count=1)

            channel.basic_consume(
                queue="analytic_queue",
                on_message_callback=show_orders,
                auto_ack=False
            )
            logger.info(" [*] Ожидаем сообщений. Для выхода нажмите CTRL+C")
            channel.start_consuming()

            