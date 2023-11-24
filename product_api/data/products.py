# products is a list of Product, should be declared as

from ..models.product import Product
from typing import List
products: List[Product] = [

  Product(id=1, name="Apple", price=20, stock=10),
  Product(id=2, name="Orange", price=15, stock=10),
]