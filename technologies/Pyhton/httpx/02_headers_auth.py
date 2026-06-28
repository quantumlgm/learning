"""
Lesson 2: HTTP Headers manipulation and API Authentication via 'httpx'.

This module demonstrates how to inject metadata into outgoing requests using
HTTP Headers. It covers spoofing the 'User-Agent' to prevent bot-detection
mechanisms and managing secret API Keys for secure endpoint authentication.

Key Concepts:
- Custom HTTP Headers: Using the 'headers' parameter to pass 'x-cg-demo-api-key'
  as a cryptographic passport directly to the server's validation layer.
- Client Identification Management: Overriding 'User-Agent' string constants
  to present the automated script as a standard web browser.
- Multi-layered JSON Extraction: Navigating complex nested data structures
  down to deep leaf nodes (e.g., dict -> list -> dict -> dict).
"""

from settings import settings

"""
There is my API token for CoinGecko requests
"""
from rich import print
import httpx
import asyncio

headers = {"User-Agent": "Firefox", "x-cg-demo-api-key": settings.TOKEN}


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.coingecko.com/api/v3/search/trending",
            headers=headers,
        )
        data = response.json()

    coins = data["coins"][:3]

    for c in coins:
        item = c["item"]
        name = item["name"]
        symbol = item["symbol"]
        price = item["data"]["price"]

        print(f"{name} ({symbol}): ${price}")


if __name__ == "__main__":
    asyncio.run(main())
    """
    The Black Bull (ANSEM): $0.08772189988020244
    XMAQUINA (DEUS): $0.029405884550104098
    Solstice (SLX): $0.5735211580654935
    """
