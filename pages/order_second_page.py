import allure
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderSecondPageLocators
from pages.base_page import BasePage

class OrderSecondPage(BasePage):
    def set_date(self, date):
        with allure.step(f'Ввести дату {date}'):
            date_field = self.find_element(OrderSecondPageLocators.DATE_FIELD)
            date_field.click()
            date_field.send_keys(date)
            self.driver.find_element(By.XPATH, f"//div[contains(@class,'react-datepicker__day') and text()='{date.split('.')[0]}']").click()

    def set_rental_period(self, period):
        with allure.step(f'Выбрать срок аренды {period}'):
            self.click_element(OrderSecondPageLocators.RENTAL_PERIOD_DROPDOWN)
            self.driver.find_element(By.XPATH, f"//div[text()='{period}']").click()

    def set_color(self, color):
        with allure.step(f'Выбрать цвет {color}'):
            if color == "black":
                self.click_element(OrderSecondPageLocators.COLOR_BLACK)
            elif color == "grey":
                self.click_element(OrderSecondPageLocators.COLOR_GREY)

    def set_comment(self, comment):
        with allure.step(f'Ввести комментарий {comment}'):
            self.send_keys_to_element(OrderSecondPageLocators.COMMENT_FIELD, comment)

    def click_order_button(self):
        with allure.step('Нажать кнопку Заказать'):
            self.click_element(OrderSecondPageLocators.ORDER_BUTTON)
