import pytest
from helpers.api import UserApi
from helpers.generator import generate_user_payload


@pytest.fixture
def user_payload():
    return generate_user_payload()

@pytest.fixture
def created_user():
    payload = generate_user_payload()
    response = UserApi.create_user(payload)

    token = None
    if response.status_code == 200:
        token = response.json()["accessToken"]

    yield payload
    
    if token:
        UserApi.delete_user(token)

@pytest.fixture
def authorized_user():
    payload = generate_user_payload()
    response = UserApi.create_user(payload)

    token = response.json()["accessToken"]

    yield token

    UserApi.delete_user(token)
