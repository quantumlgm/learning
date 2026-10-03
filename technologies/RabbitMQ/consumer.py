import json
from loguru import logger
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties
from technologies.RabbitMQ.config import get_connection

MAIN_EXCHANGE = "app_main_exchange"
MAIN_QUEUE = "tasks_main_queue"

# Очередь задержки (буфер)
RETRY_EXCHANGE = "app_retry_exchange"
RETRY_QUEUE = "tasks_retry_5s_queue"


def process_task(
    ch: BlockingChannel,
    method: Basic.Deliver,
    properties: BasicProperties,
    body: bytes
):
    data = json.loads(body.decode("utf-8"))
    attempts = data.get("attempts", 0) + 1
    data["attempts"] = attempts

    logger.warning(f"Попытка #{attempts} обработать задачу '{data['task_name']}'...")

    # Имитируем, что сервис заработает только с 3-й попытки
    if attempts < 3:
        logger.error(f"Сервис недоступен! Отправляем задачу в буфер ожидания на 5 секунд...")
        
        # Пересылаем сообщение в очередь задержки
        ch.basic_publish(
            exchange=RETRY_EXCHANGE,
            routing_key="",
            body=json.dumps(data).encode("utf-8")
        )
        # Подтверждаем исходное сообщение, чтобы удалить его из основной очереди
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        logger.success(f"Задача '{data['task_name']}' УСПЕШНО выполнена с {attempts}-й попытки!")
        ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            # 1. Основная инфраструктура
            channel.exchange_declare(exchange=MAIN_EXCHANGE, exchange_type="fanout", durable=True)
            channel.queue_declare(queue=MAIN_QUEUE, durable=True)
            channel.queue_bind(exchange=MAIN_EXCHANGE, queue=MAIN_QUEUE)

            # 2. Инфраструктура очереди задержки (Retry)
            channel.exchange_declare(exchange=RETRY_EXCHANGE, exchange_type="fanout", durable=True)
            
            # Настройка очереди ожидания:
            # - Живет 5000 мс (5 сек)
            # - По истечении TTL пересылает сообщение обратно в MAIN_EXCHANGE!
            retry_queue_args = {
                "x-message-ttl": 5000,
                "x-dead-letter-exchange": MAIN_EXCHANGE,
            }
            channel.queue_declare(
                queue=RETRY_QUEUE,
                durable=True,
                arguments=retry_queue_args
            )
            channel.queue_bind(exchange=RETRY_EXCHANGE, queue=RETRY_QUEUE)

            # 3. Слушаем только основную очередь
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(
                queue=MAIN_QUEUE,
                on_message_callback=process_task,
                auto_ack=False
            )
            logger.info("Воркер запущен. Ожидаем задачи...")
            channel.start_consuming()


if __name__ == "__main__":
    main()