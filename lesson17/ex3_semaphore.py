import asyncio
import random

sem = asyncio.Semaphore(3)

async def worker(id):
    async with sem:
        print(f"Worker {id} started")
        await asyncio.sleep(random.uniform(0.5, 2))
        print(f"Worker {id} finished")

async def main():
    tasks = [worker(i) for i in range(1, 21)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
