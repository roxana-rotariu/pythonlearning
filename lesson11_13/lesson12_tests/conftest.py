# lesson12_tests/conftest.py
import pytest
from src.models.product import Product

@pytest.fixture
def sample_product():
    return Product("Book", 50)
