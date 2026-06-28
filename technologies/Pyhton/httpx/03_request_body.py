"""
Lesson 3: HTTP POST Requests and Request Body transmission via 'httpx'.

This module demonstrates how to transmit structured state datasets to a remote 
server inside the HTTP Request Body using POST methods. It highlights the 
architectural boundary between URL-encoded form formatting and native JSON payloads.

Key Concepts:
- 'json=' Parameter: Instructs 'httpx' to automatically serialize Python dicts 
  into raw JSON strings and inject the 'Content-Type: application/json' header.
- Echo-Server Validation: Utilizing 'httpbin.org/post' to analyze incoming stream 
  mirroring and verify exact data type preservation across network hops.
- Target Leaf Extraction: Programmatically traversing nested payload keys 
  (e.g., response -> json_root -> gateway_id) without third-party reliance.
"""

from rich import print
import asyncio
import httpx

payload = {
    "gateway_id": "GW-007-TXT",
    "is_active": True,
    "temperatures": [22.5, 24.0, 21.8],
    "version": 2,
}


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.post("https://httpbin.org/post", json=payload)
    data = response.json()
    print(f"Status: {response.status_code}. ID: {data['json']['gateway_id']}")


if __name__ == "__main__":
    asyncio.run(main())
    """
    Status: 200. ID: GW-007-TXT
    """
