import asyncio
import aiohttp

class ProductAPIClient:
    BASE_URL = "https://fakestoreapi.com/products"

    async def fetch_product(self, session, product_id):
        url = f"{self.BASE_URL}/{product_id}"
        async with session.get(url) as r:
            r.raise_for_status()
            return await r.json()


class AsyncProductRepository:
    def __init__(self):
        self.cache = {}

    async def save(self, product):
        self.cache[product["id"]] = product

    async def get(self, id):
        return self.cache.get(id)


class AsyncStoreFacade:
    def __init__(self, api_client, repo):
        self.api = api_client
        self.repo = repo

    async def get_product(self, id, session):
        cached = await self.repo.get(id)
        if cached:
            print(f"FROM CACHE for {id}")
            return cached

        product = await self.api.fetch_product(session, id)
        await self.repo.save(product)
        return product


async def main():
    api = ProductAPIClient()
    repo = AsyncProductRepository()
    store = AsyncStoreFacade(api, repo)

    async with aiohttp.ClientSession() as session:
        tasks = [store.get_product(i, session) for i in range(1, 6)]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())