from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(f"[LOG] Incoming: {request.method} {request.url}")
        response = await call_next(request)
        print(f"[LOG] Status: {response.status_code}")
        return response
