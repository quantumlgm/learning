import json
from technologies.RabbitMQ.config import get_connection, logger

MAIN_EXCHANGE = "app_main_exchange"


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            payload = {"task_name": "Синхронизация с банком", "attempts": 0}
            channel.basic_publish(
                exchange=MAIN_EXCHANGE,
                routing_key="",
                body=json.dumps(payload).encode("utf-8")
            )
            logger.info("Задача отправлена в очередь")


if __name__ == "__main__":
    main()