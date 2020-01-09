import logging
from typing import List
from pony.orm import *
from app.api.models.cart import *
from app.db.base import db


@db_session
def read_cart() -> CartInResponse:
    cart: CartInResponse = {}
    items: List[OrderInResponse] = []


    try:
        rows = select(c for c in db.Cart)[:]
        for row in rows:
            item = {}
            item = row.to_dict()
            item['product'] = row.product.to_dict()
            items.append(item)

        cart['order'] = items
        cart['total'] = sum([x['price'] for x in cart['order']])
    except Exception as e:
        logging.error(e)
    return cart


@db_session
def create_product(row: Product):
    db.Product(**row.dict())
    return row


@db_session
def add_item_cart(row: Cart):
    product = db.Product.get(id=row.productId)
    if not product:
        return product
    price = product.price * row.qty
    db.Cart(price=price, qty=row.qty, product=product)
    return row
