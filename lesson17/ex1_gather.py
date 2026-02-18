import asyncio
import random

async def task(id):
    print(f"Task {id} start")
    await asyncio.sleep(random.randint(1,3))
    print(f"Task {id} end")

async def main():
    tasks = [task(i) for i in range(1, 6)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
