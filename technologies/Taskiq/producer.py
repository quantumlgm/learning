import asyncio

from tasks import broker, notify_user


async def main():
    await broker.startup()

    await (
        notify_user.kicker()
        .with_labels(
            source="payment_gateway",
            service_name="billing-service"
        )
        .kiq(user_id=101, message="Платеж успешно получен")
    )

    await broker.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
