import aiohttp
import asyncio

URL = "https://speed.hetzner.de/100MB.bin"  # fișier de test
FILE_NAME = "100MB.bin"
CHUNK_SIZE = 4096  # 4KB

async def download():
    async with aiohttp.ClientSession() as session:
        # ssl=False dezactivează verificarea certificatului
        async with session.get(URL, ssl=False) as resp:
            total = int(resp.headers.get('Content-Length', 0))
            downloaded = 0

            with open(FILE_NAME, 'wb') as f:
                async for chunk in resp.content.iter_chunked(CHUNK_SIZE):
                    f.write(chunk)
                    downloaded += len(chunk)
                    percent = downloaded * 100 / total if total else 0
                    print(f"\rDownloaded {downloaded} of {total} bytes ({percent:.2f}%)", end="")
    print("\nDownload completed.")

if __name__ == "__main__":
    asyncio.run(download())
