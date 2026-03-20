import allure
from helpers.api import UserApi
from helpers.data import ErrorMessages
from helpers.generator import generate_user_payload

@allure.suite("Изменение данных пользователя")
class TestUpdateUser:

    @allure.title("Изменение данных с авторизацией")
    def test_update_user_authorized_returns_200(self, authorized_user):
        new_data = generate_user_payload()
        response = UserApi.update_user(new_data, authorized_user)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Изменение данных без авторизации")
    def test_update_user_without_auth_returns_401(self):
        new_data = generate_user_payload()
        response = UserApi.update_user(new_data)

        assert response.status_code == 401
        assert response.json()["message"] == ErrorMessages.UNAUTHORIZED
