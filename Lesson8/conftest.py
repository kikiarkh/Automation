import requests
import pytest
from constans import Base_URL

@pytest.fixture()
def get_token(username='flora', password='nature-fairy'):
    log_pass = {
            "username": username,
            "password": password
        }
    token = requests.post(Base_URL + '/auth/login', json=log_pass)
    return token.json()["userToken"]