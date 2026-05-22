from locators.order_page_locators import OrderConfirmPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class OrderConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    def click_confirm_yes_button(self):
        self.driver.find_element(*OrderConfirmPageLocators.CONFIRM_YES_BUTTON).click()

    def get_order_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                OrderConfirmPageLocators.ORDER_SUCCESS_HEADER
            )
        ).text