BASE_URL = "https://stellarburgers.education-services.ru/api"

class Endpoints:
    create_order = f"{BASE_URL}/orders"
    get_orders = f"{BASE_URL}/orders"
    register_user = f"{BASE_URL}/auth/register"
    login_user = f"{BASE_URL}/auth/login"
    logout_user = f"{BASE_URL}/auth/logout"
    get_user_info = f"{BASE_URL}/auth/user"
    get_ingredients = f"{BASE_URL}/ingredients"
