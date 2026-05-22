from locators.order_page_locators import OrderSecondPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class OrderSecondPage:
    def __init__(self, driver):
        self.driver = driver

    def set_date(self, date):
        date_field = self.driver.find_element(*OrderSecondPageLocators.DATE_FIELD)
        date_field.click()
        date_field.send_keys(date)
        self.driver.find_element(By.XPATH, f"//div[contains(@class,'react-datepicker__day') and text()='{date.split('.')[0]}']").click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderSecondPageLocators.COMMENT_FIELD).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*OrderSecondPageLocators.ORDER_BUTTON).click()

    def set_color(self, color):
        if color == "black":
            self.driver.find_element(*OrderSecondPageLocators.COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*OrderSecondPageLocators.COLOR_GREY).click()

    def set_rental_period(self, period):
        self.driver.find_element(*OrderSecondPageLocators.RENTAL_PERIOD_DROPDOWN).click()
        self.driver.find_element(By.XPATH, f"//div[text()='{period}']").click()