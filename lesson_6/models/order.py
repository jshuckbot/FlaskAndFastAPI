from datetime import datetime

from pydantic import BaseModel, Field


class OrderIn(BaseModel):
    user_id: int = Field(default=1)
    product_id: int = Field(default=1)
    date: datetime = Field(default=datetime.now())
    status: bool = Field(default=False)


class Order(OrderIn):
    id: int
