import allure
from locators.order_page_locators import OrderConfirmPageLocators
from pages.base_page import BasePage


class OrderConfirmPage(BasePage):
    def click_confirm_yes_button(self):
        with allure.step('Нажать кнопку Да'):
            self.click_element(OrderConfirmPageLocators.CONFIRM_YES_BUTTON)

    def get_order_success_message(self):
        with allure.step('Получить сообщение об успешном заказе'):
            return self.get_text(OrderConfirmPageLocators.ORDER_SUCCESS_HEADER)
        