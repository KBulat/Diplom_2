import allure
from helpers.api import UserApi
from helpers.data import ErrorMessages

@allure.suite("Создание пользователя")
class TestCreateUser:
    
    @allure.title("Создание уникального пользователя")
    def test_create_user_with_valid_data_returns_200(self, user_payload):
        response = UserApi.create_user(user_payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

        # удаление созданного пользователя
        token = response.json()["accessToken"]
        UserApi.delete_user(token)

    @allure.title("Создание уже созданного пользователя")
    def test_create_existing_user_returns_403(self, created_user):
        response = UserApi.create_user(created_user)

        assert response.status_code == 403
        assert response.json()["message"] == ErrorMessages.USER_EXISTS

    @allure.title("Создание пользователя без заполнения обязательного поля")
    def test_create_user_without_required_field_returns_403(self, user_payload):
        user_payload.pop("email")
        response = UserApi.create_user(user_payload)

        assert response.status_code == 403
        assert response.json()["message"] == ErrorMessages.NOT_ENOUGH_DATA
