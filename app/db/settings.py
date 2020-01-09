import logging
import random as ra
from app.core import config
from decimal import (Decimal)
from .base import *

dbname = config.DB_NAME

db_params = {'provider': 'sqlite', 'filename': dbname, 'create_db': True}


def init():
    db.bind(db_params)
    try:
        db.drop_table('Cart',True,with_all_data=True)
    except Exception as e:
        logging.error("exception: {}".format(e))      
    try:
        logging.info('DB_NAME: {}'.format(config.DB_NAME))
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
            name="Product {}".format(i+1),
            description='Description {}'.format(i+1),
            price=Decimal(ra.uniform(1.00, 100.00)))


@db_session
def isPopulated():
    logging.info("checking product is populated")
    flag = db.exists('select * from Product where id = 1')
    return flag
