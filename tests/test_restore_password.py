import allure
from urls import *


@allure.suite('Тест восстановление пароля')
class TestRestorePassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_restore_password_redirection(self, main_page, restore_page, login_page):
        main_page.open(MAIN_PAGE)
        main_page.click_lk()
        main_page.assert_current_url(LOGIN_PAGE)
        login_page.click_restore_password()
        restore_page.assert_current_url(RESTORE_PAGE)
        restore_page.check_restore_password_text()

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_entering_email_and_restore(self, restore_page):
        restore_page.open(RESTORE_PAGE)
        restore_page.entering_email()
        restore_page.click_on_restore_button()
        restore_page.check_input_code_text_for_restore()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_active_restore_password_input(self, restore_page):
        restore_page.open(RESTORE_PAGE)
        restore_page.entering_email()
        restore_page.click_on_restore_button()
        restore_page.click_eye()
        restore_page.check_active_password_input()
