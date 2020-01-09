from decimal import (Decimal)
from pony.orm import *
from .base import db


class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    description = Optional(str)
    price = Required(Decimal)
    carts = Set('Cart')


class Cart(db.Entity):
    id = PrimaryKey(int, auto=True)
    product = Required(Product)
    price = Optional(Decimal)
    qty = Optional(int)
