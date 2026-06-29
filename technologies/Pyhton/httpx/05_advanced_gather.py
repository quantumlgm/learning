from rich import print
import httpx
import asyncio

limits = httpx.Limits(max_connections=2)
timeout = httpx.Timeout(5)

async def fetch(client: httpx.AsyncClient, coin: str):
    try:
        params = {"ids": coin, "vs_currencies": "usd", "localization": False}

        response = await client.get(f"https://api.coingecko.com/api/v3/coins/{coin}", params=params)
        response.raise_for_status()
        
        data = response.json()            
        return {
            "Coin": {
                "id": data["id"],
                "price": data['market_data']['current_price']['usd']
            }
        }
    except Exception as e:
        print(f"Error: {e}")
        return

async def main():
    async with httpx.AsyncClient(limits=limits, timeout=timeout) as client:
        coins = ["bitcoin", "ethereum", "solana", "ripple"]
        tasks = [fetch(client, coin) for coin in coins]
        result = await asyncio.gather(*tasks)

        print(result)

if __name__ == "__main__":
    asyncio.run(main())
    """
    [
        {'Coin': {'id': 'bitcoin', 'price': 59665}},
        {'Coin': {'id': 'ethereum', 'price': 1571.32}},
        {'Coin': {'id': 'solana', 'price': 73.45}},
        {'Coin': {'id': 'ripple', 'price': 1.052}}
    ]
    """