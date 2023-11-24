import pytest
from fastapi.testclient import TestClient

from product_api.main import app
from product_api.models.product import Product

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_create_product():
    product = Product(id=3, name="Test", price=10, stock=10)
    response = client.post("/products", json=product.model_dump())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert product.model_dump() in response.json()

def test_update_product():
    product = Product(id=1, name="Updated", price=20, stock=20)
    response = client.put("/products/1", json=product.model_dump())
    assert response.status_code == 200
    assert response.json() == product.model_dump()

def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Product has been deleted successfully"}

@pytest.mark.parametrize(
    "product_data, expected_status",
    [
        ({"id": 4, "name": "Test", "price": 10, "stock": 10}, 200),
        ({"id": 1, "name": "Test", "price": -10, "stock": 10}, 422),
        ({"id": 1, "name": "Test", "price": 10, "stock": -10}, 422),
    ],
)
def test_create_product_parametrized(product_data, expected_status):
    response = client.post("/products", json=product_data)
    assert response.status_code == expected_status