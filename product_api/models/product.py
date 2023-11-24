from pydantic import BaseModel, validator, field_validator

class Product(BaseModel):
  id: int
  name: str
  price: float
  stock: int


  @field_validator('price', 'stock')
  def check_positive(cls, value):
      if value < 0:
          raise ValueError('must be a positive number')
      return value

  @field_validator('name')
  def check_name(cls, value):
    if value == '' or value == None:
      raise ValueError('name cannot be empty')
    # to lower case
    return value.lower()


