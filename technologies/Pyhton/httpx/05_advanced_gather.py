from rich import print
import httpx
import asyncio


limit = httpx.Limits(max_connections=2)
timeout = httpx.Timeout(5)

async def fetch(client: httpx.AsyncClient, coin: str):
    try:
        params = {"ids": coin, "vs_currencies": "usd"}

        response = await client.get("https://api.coingecko.com/api/v3/simple/price", params=params)
        response.raise_for_status()
        
        data = response.json()
        return f"Coin: {data}"
    except Exception as e:
        print(f"Error: {e}")
        return

async def main():
    async with httpx.AsyncClient() as client:
        coins = ["bitcoin", "ethereum", "solana", "ripple"]
        tasks = [fetch(client, coin) for coin in coins]
        result = await asyncio.gather(*tasks)

        print(result)

if __name__ == "__main__":
    asyncio.run(main())