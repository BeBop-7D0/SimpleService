from typing import List
import asyncio
from aiohttp import ClientSession, ClientConnectorError, ClientResponseError, ContentTypeError


async def send_tasks(target_url: str, urls: List[str] = []):
    try: 
        async with ClientSession(target_url) as session:
            async with session.get("/tasks") as response:
                body = await response.json()
                status = response.status
                response.raise_for_status()
                print(f"Status: {status}, body: {body}")

    except ContentTypeError as _:
        print("Expect json body. Got different type")
    except ClientConnectorError as _:
        print(f"Cannot connect to {target_url}")
    except ClientResponseError as _:
        print(f"Error: Status {status}, body {body}")



async def main():
    await send_tasks("http://localhost:8000")


if __name__ == "__main__":
    asyncio.run(main())