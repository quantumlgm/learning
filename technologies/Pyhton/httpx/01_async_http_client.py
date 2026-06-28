"""
Lesson 1: HTTP GET Requests and Query Parameters handling via 'httpx'.

This module demonstrates how to interact with external REST APIs using
asynchronous HTTP GET requests. It focuses on using structured query
parameters ('params') instead of manual URL string manipulation, ensuring
proper URL-encoding for safe network transmissions.

Key Concepts:
- 'httpx.AsyncClient()': Used as an asynchronous context manager to maintain
  a persistent connection pool (Keep-Alive), optimizing socket reuse.
- Query Parameters Mapping: Dictionary-based 'params' arguments automatically
  format and append key-value filters directly to the request URI string.
- Built-in JSON Parsing: Utilizing 'response.json()' to instantly transform
  the raw HTTP response body into native Python lists and dictionaries.
"""

import httpx
import asyncio
import json
from rich import print

params = {"ids": "bitcoin,ethereum,solana", "vs_currency": "usd"}


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.coingecko.com/api/v3/coins/markets", params=params
        )
        data = response.json()
    result = []

    for coin in data:
        result.append(
            {
                "id": coin["id"],
                "price": coin["current_price"],
                "market_cap": coin["market_cap"],
            }
        )

    return result


if __name__ == "__main__":
    print(asyncio.run(main()))
    """
    [
    {'id': 'bitcoin', 'price': 59553, 'market_cap': 1194243586520},
    {'id': 'ethereum', 'price': 1566.62, 'market_cap': 189131649133},
    {'id': 'solana', 'price': 71.41, 'market_cap': 41482702927}
    ]
    """
