import asyncio
import aiohttp

async def fetch_with_retry(url):
    delays = [0.5, 1, 2]
    for attempt, delay in enumerate(delays, 1):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    resp.raise_for_status()
                    text = await resp.text()
                    print(f"Success on attempt {attempt}")
                    return text
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt == len(delays):
                print("All retries failed.")
                return None
            await asyncio.sleep(delay)

async def main():
    url = "http://invalid-url.test/"
    await fetch_with_retry(url)

if __name__ == "__main__":
    asyncio.run(main())
