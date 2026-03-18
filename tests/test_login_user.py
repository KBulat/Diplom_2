import allure
from helpers.api import UserApi
from helpers.data import ErrorMessages, Credentials

@allure.suite("Логин пользователя")
class TestLoginUser:

    @allure.title("Логин под  существующим пользователем")
    def test_login_with_existing_user_returns_200(self, created_user):
        payload = {
            "email": created_user["email"],
            "password": created_user["password"]
        }

        response = UserApi.login_user(payload)

        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title("Логин с неверными данными")
    def test_login_with_wrong_credentials_returns_401(self):
        payload = {
            "email": Credentials.INVALID_EMAIL,
            "password": Credentials.INVALID_PASSWORD
        }

        response = UserApi.login_user(payload)

        assert response.status_code == 401
        assert response.json()["message"] == ErrorMessages.LOGIN_ERROR
