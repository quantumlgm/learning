import json
from technologies.RabbitMQ.config import TOPIC_EXCHANGE, get_connection, logger


def publish_event(channel, routing_key: str, data: dict):
    body = json.dumps(data).encode("utf-8")
    channel.basic_publish(
        exchange=TOPIC_EXCHANGE,
        routing_key=routing_key,
        body=body
    )
    logger.info(f"Опубликовано [{routing_key}]: {data}")


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            channel.exchange_declare(
                exchange=TOPIC_EXCHANGE,
                exchange_type="topic"
            )

            publish_event(channel, "orders.created", {"order_id": 101, "total": 4500})
            publish_event(channel, "payments.success", {"order_id": 101, "gateway": "yookassa"})
            publish_event(channel, "payments.failed", {"order_id": 102, "error": "insufficient_funds"})
            publish_event(channel, "analytics.users.click", {"button": "buy_now"})


if __name__ == "__main__":
    main()