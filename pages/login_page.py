from pages.base_page import BasePage
import locators
import allure


class LoginPage(BasePage):

    @allure.step("Клик на Восстановить пароль")
    def click_restore_password(self):
        self.click(locators.LoginPage.RESTORE_PASSWORD)

    @allure.step("Авторизация в личном кабинете")
    def login(self, email, password):
        self.click(locators.LoginPage.EMAIL_FIELD)
        self.send_input(locators.LoginPage.EMAIL_FIELD, email)
        self.click(locators.LoginPage.PASSWORD_FIELD)
        self.send_input(locators.LoginPage.PASSWORD_FIELD, password)
        self.click(locators.LoginPage.LOGIN_BUTTON)

    @allure.step("Поиск кнопки Войти")
    def check_login_button(self):
        return self.find_element(locators.LoginPage.LOGIN_BUTTON)
