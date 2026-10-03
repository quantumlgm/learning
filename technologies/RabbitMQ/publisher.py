import json
import pika
from technologies.RabbitMQ.config import get_connection, logger

EXCHANGE_NAME = "safe_exchange"
QUEUE_NAME = "safe_queue"


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            # 1. Включаем режим подтверждения доставки от брокера
            channel.confirm_delivery()

            # 2. Создаем постоянный (durable) обменник и очередь
            channel.exchange_declare(
                exchange=EXCHANGE_NAME,
                exchange_type="direct",
                durable=True
            )
            channel.queue_declare(queue=QUEUE_NAME, durable=True)
            channel.queue_bind(
                exchange=EXCHANGE_NAME,
                queue=QUEUE_NAME,
                routing_key="payment.process",
            )

            payload = {"payment_id": 999, "amount": 15000}
            body = json.dumps(payload).encode("utf-8")

            # 3. Публикуем с флагом PERSISTENT (сохранение на диск)
            is_delivered = channel.basic_publish(
                exchange=EXCHANGE_NAME,
                routing_key="payment.process",
                body=body,
                properties=pika.BasicProperties(
                    delivery_mode=pika.DeliveryMode.Persistent
                )
            )

            if is_delivered:
                logger.success(f"Платеж безопасно сохранен в брокере: {payload}")
            else:
                logger.error("Сбой! Сообщение не дошло до брокера.")


if __name__ == "__main__":
    main()