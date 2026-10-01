import json

from aio_pika import exchange
from technologies.RabbitMQ.config import (
    FANOUT_EXCHANGE,
    MQ_EXCHANGE,
    MQ_ROUTING_KEY,
    get_connection,
    logger,
)


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            channel.exchange_declare(
                exchange=FANOUT_EXCHANGE,
                exchange_type="fanout"
            )

            payload = {
                "post_id": 42,
                "title": "Уроки по RabbitMQ",
                "author": "Сурен"
            }
            body = json.dumps(payload).encode("utf-8")

            channel.basic_publish(
                exchange=FANOUT_EXCHANGE,
                routing_key="",
                body=body
            )
            logger.info(f"Отправлено сообщение: {payload}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("Паблишер остановлен.")
