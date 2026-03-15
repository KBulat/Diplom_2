import requests
from helpers.endpoints import Endpoints

class UserApi:
    def create_user(payload):
        return requests.post(Endpoints.register_user, json=payload)

    def login_user(payload):
        return requests.post(Endpoints.login_user, json=payload)

    def update_user(payload, token=None):
        headers = {}
        if token:
            headers = {"Authorization": token}
        return requests.patch(Endpoints.get_user_info, json=payload, headers=headers)
    
    def delete_user(token):
        headers = {"Authorization": token}
        return requests.delete(Endpoints.get_user_info, headers=headers)
    
class OrderApi:
    def create_order(payload, token=None):
        headers = {}
        if token:
            headers = {"Authorization": token}

        return requests.post(Endpoints.create_order, json=payload, headers=headers)
    
    def get_orders(token=None):
        headers = {}
        if token:
            headers = {"Authorization": token}

        return requests.get(Endpoints.get_orders, headers=headers)
