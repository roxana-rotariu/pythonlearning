import pytest
from src.models.product import Product

@pytest.fixture
def product():
    return Product("Laptop", 1000)

def test_discount(product):
    product.apply_discount(10)
    assert product.price == 900
    
    