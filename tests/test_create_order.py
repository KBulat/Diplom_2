import allure
from helpers.api import OrderApi
from helpers.data import ErrorMessages, INGREDIENTS_HASH

@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Cоздание заказа с авторизацией")
    def test_create_order_authorized_returns_200(self, authorized_user):
        payload = {"ingredients": INGREDIENTS_HASH}

        response = OrderApi.create_order(payload, authorized_user)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized_returns_200(self):
        payload = {"ingredients": INGREDIENTS_HASH}

        response = OrderApi.create_order(payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_returns_400(self):
        payload = {"ingredients": []}

        response = OrderApi.create_order(payload)

        assert response.status_code == 400
        assert response.json()["message"] == ErrorMessages.INGREDIENT_IDS_NOT_PROVIDED

    @allure.title("Создание заказа с невалидным хешем")
    def test_create_order_with_invalid_hash_returns_500(self):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6z"]}

        response = OrderApi.create_order(payload)

        assert response.status_code == 500


