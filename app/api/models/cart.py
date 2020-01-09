from decimal import (Decimal)
from typing import (List)
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    description: str
    price: Decimal


class Cart(BaseModel):
    productId: int
    qty: int = Field(..., gt=0,
                     description="The qty must be greater than zero")


class OrderInResponse(BaseModel):
    product: Product
    price: Decimal
    qty: int


class CartInResponse(BaseModel):
    order: List[OrderInResponse] = []
    total: Decimal
