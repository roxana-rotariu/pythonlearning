from fastapi import FastAPI
from app.api.routes.user_routes import router as user_router
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI()
app.add_middleware(LoggingMiddleware)
app.include_router(user_router)
