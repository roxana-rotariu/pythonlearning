from fastapi import APIRouter
from app.schemas.product_schema import ProductCreate, ProductRead

router = APIRouter(prefix="/products")

fake_db = []

@router.post("", response_model=ProductRead)
async def create_product(product: ProductCreate):
    new = {"id": len(fake_db)+1, **product.dict()}
    fake_db.append(new)
    return new