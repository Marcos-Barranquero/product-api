from .models.product import Product

def playground():
  possible_product = {
    "id": "1",
    "name": "Pear",
    "price": 10,
    "stock": -1
  }

  try:
    processed_product = Product(**possible_product)
    print(processed_product)
  except Exception as e:
    print(e)


if __name__ == "__main__":
  playground()