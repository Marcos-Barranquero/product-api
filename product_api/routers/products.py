from typing import Optional

from fastapi import APIRouter, HTTPException

from redis import Redis

import json

from ..data.products import products
from ..models.product import Product

product_router = APIRouter()

redis = Redis(host='redis', port=6379)

products_for_cache: list[Product] = products


@product_router.get("/products")
def get_products() -> list[Product]:

    cached_products = redis.json().get('products')

    if cached_products is None:
        products_json = json.dumps([product.model_dump_json() for product in products])
        redis.set('products', products_json)
        return products
    else:
        product_dicts = json.loads(cached_products)
        return [Product(**product_dict) for product_dict in product_dicts]


@product_router.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int) -> Optional[Product]:
    product = next((product for product in products if product.id == product_id), None)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@product_router.post("/products")
def create_product(product: Product) -> list[Product]:
  if product in products:
    raise HTTPException(status_code=409, detail="Product already exists")
  # validation is implicit, use pydantic to restrict domain, price and stock to positive numbers
  products.append(product)
  return products

@product_router.put("/products/{product_id}")
def update_product(product_id: int, product: Product) -> Product:
    existing_product: Product | None = next((p for p in products if p.id == product_id), None)

    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    # Update the product details
    existing_product.name = product.name
    existing_product.price = product.price
    existing_product.stock = product.stock

    return existing_product


@product_router.delete("/products/{product_id}")
def delete_product(product_id: int) -> dict[str, str]:
    existing_product: Product | None = next((p for p in products if p.id == product_id), None)

    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    products.remove(existing_product)
    return {"message": "Product has been deleted successfully"}