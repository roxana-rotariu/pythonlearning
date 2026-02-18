import asyncio

async def producer(queue):
    for i in range(10):
        print(f"Producing item {i}")
        await queue.put(i)
        await asyncio.sleep(0.1)
    await queue.put(None)  # Sentinel to stop consumer

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            print("Consumer received sentinel, exiting")
            break
        print(f"Consuming item {item}")
        await asyncio.sleep(0.2)

async def main():
    queue = asyncio.Queue()
    prod = asyncio.create_task(producer(queue))
    cons = asyncio.create_task(consumer(queue))
    await asyncio.gather(prod, cons)

if __name__ == "__main__":
    asyncio.run(main())
