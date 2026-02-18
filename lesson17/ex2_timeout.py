import asyncio

async def slow_function():
    print("Starting slow function...")
    await asyncio.sleep(3)
    print("Slow function finished.")

async def main():
    try:
        await asyncio.wait_for(slow_function(), timeout=1)
    except asyncio.TimeoutError:
        print("Timeout! The function took too long.")

if __name__ == "__main__":
    asyncio.run(main())
