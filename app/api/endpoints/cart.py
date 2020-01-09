
from fastapi import APIRouter

from fastapi.encoders import jsonable_encoder
from app.core.utils import create_aliased_response
from app.repository import cart as db
from app.api.models.cart import *

from typing import List
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

router = APIRouter()


@router.get("/", response_model=CartInResponse, status_code=HTTP_200_OK)
def read_items_cart():
    rows = db.read_cart()
    return rows


@router.post("/", status_code=HTTP_200_OK)
def add_items(item: Cart):
    row = db.add_item_cart(item)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Product not exist")
    return db.add_item_cart(item)
