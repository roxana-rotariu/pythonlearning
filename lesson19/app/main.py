from fastapi import FastAPI
from app.api.product_routes import router as product_router
from app.api import user_routes

app = FastAPI()

app.include_router(product_router)
app.include_router(user_routes.router)