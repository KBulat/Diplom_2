from faker import Faker

fake = Faker("ru_RU")

def generate_user_payload():
    return {
        "email": fake.email(),
        "password": fake.password(length=8, special_chars=True, digits=True),
        "name": fake.name()
    }