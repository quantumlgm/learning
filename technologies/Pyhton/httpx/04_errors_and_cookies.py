"""
Lesson 4: HTTP Status Codes validation, Exception Handling, and Cookies via 'httpx'.

This module demonstrates defensive programming techniques when interacting with
unstable remote infrastructures. It covers intercepting server-side and client-side
HTTP errors using structured try-except blocks, while maintaining state via Cookies.

Key Concepts:
- 'response.raise_for_status()': Explicitly forces 'httpx' to raise an
  'httpx.HTTPStatusError' if the received status code falls into 4xx or 5xx ranges.
- Exception Hierarchy: Catching granular network anomalies ('httpx.RequestError')
  separately from response code failures ('httpx.HTTPStatusError').
- State Persistence: Injecting key-value tracking pairs using the 'cookies'
  parameter to mimic session authentication on target servers.
"""

from rich import print
import asyncio
import httpx
import random

cookies = {"user_session_token": "123-SvjwEff-#@!"}


async def main():
    choice = random.choice([True, False])
    """
    With a 50-50 chance we get random selection 
    of True and False, and this depends on
    the next response to the status code
    """

    async with httpx.AsyncClient() as client:
        try:
            if not choice:
                response = await client.get(
                    "https://httpbin.org/status/500", cookies=cookies
                )
            else:
                response = await client.get(
                    "https://httpbin.org/status/200", cookies=cookies
                )
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(f"Server error. Status code: {e.response.status_code}")
            return
        except httpx.RequestError as e:
            print(f"Network error. Status code: {e.response.status_code}")
            return
        except Exception as e:
            print(f"Unknown error. Status code: {e.response.status_code}")
            return
    print("[bold green]✓[/bold green] Successfully reached the endpoint")


if __name__ == "__main__":
    asyncio.run(main())
    """
    So if choice have True we get: ✓ Successfully reached the endpoint
    But if choice is False: Server error. Status code: Server error '500 INTERNAL SERVER ERROR' for url 'https://httpbin.org/status/500'
    """
