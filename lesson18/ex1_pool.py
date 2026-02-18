import asyncio
import aiohttp

async def fetch(session, i):
    print(f"Starting request {i}")
    async with session.get("https://httpbin.org/delay/2") as resp:
        await resp.text()
    print(f"Finished request {i}")

async def main():
    connector = aiohttp.TCPConnector(limit=5)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch(session, i) for i in range(10)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
