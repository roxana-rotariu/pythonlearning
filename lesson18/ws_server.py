from aiohttp import web, WSMsgType

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            reply = f"Echo: {msg.data}"
            await ws.send_str(reply)
        elif msg.type == WSMsgType.ERROR:
            print(f"WebSocket connection closed with exception {ws.exception()}")

    print("WebSocket connection closed")
    return ws

app = web.Application()
app.add_routes([web.get('/ws', websocket_handler)])

if __name__ == "__main__":
    web.run_app(app)
