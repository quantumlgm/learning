from rich import print
import asyncio
import httpx 

payload = {
    "gateway_id": "GW-007-TXT",
    "is_active": True,
    "temperatures": [22.5, 24.0, 21.8],
    "version": 2
}

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://httpbin.org/post",
            json=payload            
        )
    data = response.json()
    print(f"Status: {response.status_code}. ID: {data["json"]["gateway_id"]}")

if __name__ == "__main__":
    asyncio.run(main())
    """
    Status: 200. ID: GW-007-TXT
    """
