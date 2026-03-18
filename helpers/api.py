import allure
import requests
from helpers.endpoints import Endpoints

class UserApi:

    @allure.step("Создание пользователя")
    def create_user(payload):
        return requests.post(Endpoints.register_user, json=payload)

    @allure.step("Логин пользователя")
    def login_user(payload):
        return requests.post(Endpoints.login_user, json=payload)

    @allure.step("Обновление данных пользователя")
    def update_user(payload, token=None):
        headers = {}
        if token:
            headers = {"Authorization": token}
        return requests.patch(Endpoints.get_user_info, json=payload, headers=headers)
    
    @allure.step("Удаление пользователя")
    def delete_user(token):
        headers = {"Authorization": token}
        return requests.delete(Endpoints.get_user_info, headers=headers)
    
class OrderApi:
    @allure.step("Создание заказа")
    def create_order(payload, token=None):
        headers = {}
        if token:
            headers = {"Authorization": token}

        return requests.post(Endpoints.create_order, json=payload, headers=headers)
    
    @allure.step("Получение списка заказов")
    def get_orders(token=None):
        headers = {}
        if token:
            headers = {"Authorization": token}

        return requests.get(Endpoints.get_orders, headers=headers)
