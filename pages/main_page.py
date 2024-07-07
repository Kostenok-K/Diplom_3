from pages.base_page import BasePage
import locators
import allure


class MainPage(BasePage):

    @allure.step("Клик на Личный кабинет")
    def click_lk(self):
        self.click(locators.MainPage.ACCOUNT_LINK)

    @allure.step("Клик на Конструктор")
    def click_on_constructor(self):
        self.click(locators.MainPage.CONSTRUCTOR_LINK)

    @allure.step("Клик на Лента заказов")
    def click_on_order_feed(self):
        self.click(locators.MainPage.ORDER_FEED)

    @allure.step("Клик на ингредиент")
    def click_on_ingredient(self):
        self.click(locators.MainPage.BUN_INGREDIENT)

    @allure.step("Клик на крестик закрытия")
    def click_on_close_button(self):
        self.click(locators.MainPage.CLOSE)

    @allure.step("Проверка деталей ингредиента")
    def check_details(self):
        for elements in [locators.MainPage.BUN_INGREDIENT, locators.MainPage.DETAILS, locators.MainPage.CLOSE]:
            find = self.find_element(elements)
            assert find.is_displayed()

    @allure.step("Проверка закрытия всплывающего окна с деталями")
    def check_close_details_popup(self):
        popup = self.find_element(locators.MainPage.POPUP)
        visibility = popup.get_attribute("visibility")
        assert visibility != "visible"

    @allure.step("Создание заказа")
    def make_order(self):
        bun = self.find_element(locators.MainPage.BUN_INGREDIENT)
        sauce = self.find_element(locators.MainPage.SAUCE_INGREDIENT)
        topping = self.find_element(locators.MainPage.TOPPING_INGREDIENT)
        my_burger = self.find_element(locators.MainPage.MY_BURGER)
        for i in [bun, sauce, topping]:
            self.drag_and_drop(i, my_burger)
        self.click(locators.MainPage.ORDER_BUTTON)

    @allure.step("Проверка оформления заказа")
    def check_my_order(self):
        if self.find_element(locators.MainPage.ORDER_PLACED):
            return True

    @allure.step("Получение счетчика ингредиента")
    def get_ingredient_counter(self):
        counter = self.get_text(locators.MainPage.INGREDIENT_COUNTER)
        return counter
