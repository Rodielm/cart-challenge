from fastapi import APIRouter

from .endpoints.cart import router as cart_router

router = APIRouter()

router.include_router(cart_router, prefix="/cart", tags=["Cart"])
