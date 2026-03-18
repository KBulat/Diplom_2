class ErrorMessages:
    INGREDIENT_IDS_NOT_PROVIDED = "Ingredient ids must be provided"
    USER_EXISTS = "User already exists"
    NOT_ENOUGH_DATA = "Email, password and name are required fields"
    LOGIN_ERROR = "email or password are incorrect"
    UNAUTHORIZED = "You should be authorised"

class Credentials:
    INVALID_EMAIL = "wrong_email@gmail.com"
    INVALID_PASSWORD = "WrongPassword123"

INGREDIENTS_HASH = [
    "61c0c5a71d1f82001bdaaa6d", # Флюоресцентная булка R2-D3
    "61c0c5a71d1f82001bdaaa6c", # Краторная булка N-200i
    "61c0c5a71d1f82001bdaaa72"  # Соус Spicy-X
    ]

INVALID_INGREDIENT_HASH = "61c0c5a71d1f82001bdaaa6z"