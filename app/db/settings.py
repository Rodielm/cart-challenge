import logging
import random as ra
from decimal import (Decimal)
from .base import *

db_params = {'provider': 'sqlite', 'filename': 'cartdb.db', 'create_db': True}


def init():
    db.bind(db_params)
    try:
        logging.info("initilize database")
        db.generate_mapping(create_tables=True)
        if isPopulated() is False:
            populate_database()
    except Exception as e:
        logging.error("exception: {}".format(e))


@db_session
def populate_database():
    logging.info("populating database...")
    for i in range(20):
        db.Product(
            name="Product {}".format(i),
            description='Description {}'.format(i),
            price=Decimal(ra.uniform(1.00, 100.00)))
    logging.info("Products -- ".format(db.Product.select()))
    commit()
    pro = db.Product[1]
    db.Cart(product=pro,price=pro.price,qty=1)
    commit()


@db_session
def isPopulated():
    logging.info("checking product is populated")
    flag = db.exists('select * from Product where id = 1')
    return flag
