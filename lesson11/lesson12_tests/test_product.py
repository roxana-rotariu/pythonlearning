# lesson12_tests/test_product.py
import pytest
from src.models.product import Product
from unittest.mock import Mock

def test_apply_discount(sample_product):
    sample_product.apply_discount(10)
    assert sample_product.price == 45  # 50 - 10%

def test_str_output(sample_product, capsys):
    print(sample_product)  # folosește __str__ sau __repr__
    captured = capsys.readouterr()
    assert "Book" in captured.out
    assert "50" in captured.out

def test_mock_repository():
    # simulăm un repo care returnează un Product
    mock_repo = Mock()
    mock_repo.get_product.return_value = Product("Laptop", 1000)

    p = mock_repo.get_product()
    assert p.name == "Laptop"
    assert p.price == 1000
    mock_repo.get_product.assert_called_once()
