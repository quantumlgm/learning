"""

"""

from typing import Final, Any

payment_gateway: Final[str] = "GATEWAY_ID"
service_fee: Final[float] = 0.02

# We can use registry: list[Union[str, int]] = []
Registry = list[str | int]

Transaction_record = tuple[str, int | float, str]

User_wallet = dict[str, int | float]

External_response = Any

if __name__ == "__main__":
    ruslan: Registry = ["184a754162e24", 200]
    print(ruslan)  # ['184a754162e24', 200]

    ruslan_wallet: User_wallet = {"USD": 1000, "EURO": 200}
    print(ruslan_wallet)  # {'USD': 1000, 'EURO': 200}

    ruslan_transaction: Transaction_record = ("TXN-2026-06-14", 300, "APPROVED")
    print(ruslan_transaction)  # ('TXN-2026-06-14', 300, 'APPROVED')

    weather_api_respone: External_response = ["clear_sky", 23.4, "low_solar_activity"]
    if isinstance(weather_api_respone, str):
        print(len(weather_api_respone))
    else:
        print(weather_api_respone) # ['clear_sky', 23.4, 'low_solar_activity']