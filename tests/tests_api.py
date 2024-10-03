"""
Тестирование API
"""
import allure
import requests
import pytest
from api_data import *

@pytest.fixture(scope="class")
def token():
    res = requests.post(BASE_URL+'api/token/', {"tg_id": "11"})
    result = res.json()
    token = result['access']
    return token

@allure.title("Тестирование получения пользователей")
# @pytest.mark.smoke
class TestApiUsers:
    @allure.title("Запрос списка всех пользователей")
    @allure.testcase("","TC-DE-API-USERS-001")
    def test_get_users(self, token):
        headers = {'Authorization': 'Bearer ' + token}
        res = requests.get(BASE_URL+'api/users/', headers=headers)
        with allure.step("Код ответа = 200"):
            assert res.status_code == 200
        with allure.step("Content-Type = json"):
            assert res.headers['Content-Type'] == "application/json"
        with allure.step("Дата присутствует в заголовке"):
            assert len(res.headers['date']) > 1
        data = res.json()
        with allure.step(f"Запрос вернул одну или несколько записей"):
            assert len(data) > 0
