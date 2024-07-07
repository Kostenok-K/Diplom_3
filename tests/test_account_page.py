import allure
from urls import *


@allure.suite('Тест личного кабинета')
class TestAccountPage:
    @allure.title("Переход по клику на Личный кабинет")
    def test_go_to_account_page(self, main_page, login_page, account_page, register_new_user):
        user_data = register_new_user
        login_page.open(LOGIN_PAGE)
        login_page.login(user_data.get("email"), user_data.get("password"))
        main_page.click_lk()
        account_page.check_opened_account_page()

    @allure.title("Переход в раздел История заказов")
    def test_go_to_orders_history(self, main_page, login_page, account_page, register_new_user):
        user_data = register_new_user
        login_page.open(LOGIN_PAGE)
        login_page.login(user_data.get("email"), user_data.get("password"))
        main_page.click_lk()
        account_page.check_order_history_inactive()
        account_page.click_on_orders_history()
        account_page.check_order_history_active()

    @allure.title("Выход из аккаунта")
    def test_exit(self, main_page, login_page, account_page, register_new_user):
        user_data = register_new_user
        login_page.open(LOGIN_PAGE)
        login_page.login(user_data.get("email"), user_data.get("password"))
        main_page.click_lk()
        account_page.click_exit()
        login_page.check_login_button()
