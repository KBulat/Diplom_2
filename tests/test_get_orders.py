import allure
from helpers.api import OrderApi
from helpers.data import ErrorMessages

@allure.suite("Получение заказов пользователя")
class TestGetUserOrders:

    @allure.title("Получение заказа авторизованного пользователя")
    def test_get_orders_authorized_user_returns_200(self, authorized_user):
        response = OrderApi.get_orders(authorized_user)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Получение заказа неавторизованного пользователя")
    def test_get_orders_unauthorized_user_returns_401(self):
        response = OrderApi.get_orders()

        assert response.status_code == 401
        assert response.json()["message"] == ErrorMessages.UNAUTHORIZED
