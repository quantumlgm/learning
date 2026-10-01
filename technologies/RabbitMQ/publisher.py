import json

from technologies.RabbitMQ.config import EXCHANGE, get_connection


def create_order(
    ch, 
    routing_key: str, 
    order_id: int, 
    cost: int
):
    payload = {"order_id": order_id, "cost": cost}
    body = json.dumps(payload).encode("utf-8")
    ch.basic_publish(
        exchange=EXCHANGE,
        routing_key=routing_key,
        body=body,        
    )


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            channel.exchange_declare(
                exchange="order_exchange",
                exchange_type="topic"                
            )

            create_order(channel, "order.msk.pizza.created", 1, 1000)
            create_order(channel, "order.msk.sushi.delivered", 2, 900)
            create_order(channel, "order.spb.burger.created", 3, 700)
            create_order(channel, "order.spb.pizza.cancelled", 4, 1000)

