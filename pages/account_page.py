import allure

import locators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Проверка, что открылась страница личного кабинета")
    def check_opened_account_page(self):
        element = self.find_element(locators.AccountPage.PROFILE_IN_ACCOUNT)
        assert element.is_displayed()

    @allure.step("Клик на История заказов")
    def click_on_orders_history(self):
        self.click(locators.AccountPage.ORDERS_HISTORY)

    @allure.step("Клик Выход")
    def click_exit(self):
        self.click(locators.AccountPage.EXIT_BUTTON)

    @allure.step('Проверка, что таб История заказов неактивен')
    def check_order_history_inactive(self):
        return self.find_element(locators.AccountPage.ORDER_HISTORY_INACTIVE)

    @allure.step('Проверка, что таб История заказов активен')
    def check_order_history_active(self):
        return self.find_element(locators.AccountPage.ORDER_HISTORY_ACTIVE)
