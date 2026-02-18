from aiohttp import web
import json

async def handle_hello(request):
    return web.Response(text="Hello!")

async def handle_sum(request):
    data = await request.json()
    numbers = data.get("numbers", [])
    result = sum(numbers)
    return web.json_response({"sum": result})

app = web.Application()
app.add_routes([
    web.get('/hello', handle_hello),
    web.post('/sum', handle_sum)
])

if __name__ == "__main__":
    web.run_app(app)
