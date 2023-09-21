from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    name: str = Field(title='Name product', max_length=128)
    description: str = Field(title='Description', max_length=400)
    price: int = Field(title='Price', gt=0, description="The price must be greater than zero")
    is_stock: bool = Field(default=True, title='In stock')


class Product(ProductIn):
    id: int
