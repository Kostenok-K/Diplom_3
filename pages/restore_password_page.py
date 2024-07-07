from pages.base_page import BasePage
import locators
import allure


class RestorePage(BasePage):

    @allure.step("Проверка текста в поле Восстановления пароля")
    def check_restore_password_text(self):
        actual_text = self.get_text(locators.RestorePage.RESTORE_PASSWORD_TEXT)
        assert actual_text == 'Восстановление пароля'

    @allure.step("Ввод email")
    def entering_email(self):
        self.click(locators.RestorePage.RESTORE_EMAIL_FIELD)
        self.send_input(locators.RestorePage.RESTORE_EMAIL_FIELD, 'kostenokkirill@yandex.ru')

    @allure.step("Клик на кнопку Восстановления пароля")
    def click_on_restore_button(self):
        self.click(locators.RestorePage.RESTORE_BUTTON)
        self.wait_until_invisibility_element(locators.RestorePage.RESTORE_BUTTON)

    @allure.step("Проверка текста в поле для получения кода из письма")
    def check_input_code_text_for_restore(self):
        actual_text = self.get_text(locators.RestorePage.CODE_INPUT)
        assert actual_text == 'Введите код из письма'

    @allure.step("Клик на показать/скрыть пароль")
    def click_eye(self):
        self.click(locators.RestorePage.EYE)

    @allure.step("Проверка активности поля для ввода пароля")
    def check_active_password_input(self):
        element = self.find_element(locators.RestorePage.RESTORE_PASSWORD_ACTIVE_INPUT)
        assert element.is_displayed()
