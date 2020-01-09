
import requests

from starlette.testclient import TestClient
from app.main import app
from app.api.models.cart import *

api = "http://0.0.0.0/api/v1"


def test_add_item():
    expected = {'productId': 4, 'qty': 3}
    response = requests.post(f"{api}/cart", json=expected)
    assert response.status_code == 200
    assert response.json() == expected

def test_read_items():
    response = requests.get(f"{api}/cart")
    assert response.status_code == 200

def test_add_item_not_exits():
    data = {'productId': 0, 'qty': 1}
    response = requests.post(f"{api}/cart", json=data)
    assert response.status_code == 404

def test_add_invalid_item():
    data = {'productId': 0, 'qty': 0}
    response = requests.post(f"{api}/cart",json=data)
    assert response.status_code == 422


