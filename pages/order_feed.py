from pages.base_page import BasePage
import locators
import allure


class OrderFeed(BasePage):

    @allure.step("Клик на последний заказ")
    def click_on_last_order(self):
        self.click(locators.OrderFeed.ORDER)

    @allure.step("Проверка всплвающего окна с деталями заказа")
    def check_details_popup(self):
        for elements in [locators.OrderFeed.NUMBER_ORDER_FROM_FEED, locators.OrderFeed.CONTAIN,
                         locators.OrderFeed.CONTAINING_ELEMENTS, locators.OrderFeed.STATUS]:
            find = self.find_element(elements)
            assert find.is_displayed()

    @allure.step("Проверка, что номер заказа есть в Истории заказов и в Ленте заказов")
    def check_order_number_in_list(self, number):
        history_text = self.get_order_number_in_feed()
        feed_text = self.get_order_number_in_feed()
        for i in [history_text, feed_text]:
            if number in i:
                return True
            else:
                return False

    @allure.step("Проверка, что номер заказа есть в разделе В работе")
    def check_order_number_in_progress(self, number):
        self.wait_until_invisibility_element(locators.OrderFeed.LABEL_ALL_ORDERS_ARE_READY)
        order_locator = self.concat_locator_and_number(locators.OrderFeed.ORDER_LIST, number)
        if self.find_element(order_locator):
            return True
        else:
            return False

    @allure.step('Получение номера последнего заказа в ленте')
    def get_order_number_in_feed(self):
        element = self.find_element(locators.OrderFeed.ORDER_IN_ORDER_FEED)
        return element.text

    @allure.step("Получение количества выполненных заказов за сегодня")
    def get_number_of_orders_today(self):
        number = self.get_text(locators.OrderFeed.COMPLETED_ORDERS_TODAY_BEFORE)
        return number
