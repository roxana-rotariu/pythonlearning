import asyncio
import aiohttp

semaphore = asyncio.Semaphore(2)

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/status/500"
]

async def fetch(session, url):
    retries = 3
    for attempt in range(1, retries + 1):
        async with semaphore:
            try:
                async with session.get(url) as response:
                    print(f"URL: {url} - Status: {response.status}")
                    if response.status == 200:
                        return await response.text()
                    else:
                        raise aiohttp.ClientResponseError(
                            status=response.status,
                            request_info=response.request_info,
                            history=response.history
                        )
            except Exception as e:
                print(f"Attempt {attempt} for {url} failed: {e}")
                if attempt == retries:
                    print(f"Failed to fetch {url} after {retries} attempts.")
                else:
                    await asyncio.sleep(1)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
