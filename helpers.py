import json
import random
import allure
import requests
from urls import *


@allure.step("Cоздание заказа")
def create_order_by_api(user_data):
    payload = {
        "email": user_data.get("email"),
        "password": user_data.get("password")
    }
    response = requests.post(URL_API_LOGIN, headers={"Content-type": "application/json"},
                             data=json.dumps(payload))
    token = response.json()["accessToken"]
    order = requests.post(URL_API_PLACE_ORDER,
                          headers={"Content-type": "application/json", "Authorization": f'{token}'},
                          data=json.dumps(order_data))
    number = order.json()["order"]["number"]
    return f'#0{number}'


def generate_new_user_data():
    user_data = {"email": f'user{random.randint(100, 999)}@gmail.ru',
                 "password": f'qwerty{random.randint(100000, 999999)}',
                 "name": 'Kirill'}
    return user_data


order_data = {
    "ingredients": [
        "61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa6f",
        "61c0c5a71d1f82001bdaaa72"
    ]
}
