from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderFirstPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class OrderFirstPage:
    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*OrderFirstPageLocators.NAME_FIELD).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*OrderFirstPageLocators.LAST_NAME_FIELD).send_keys(last_name)
    
    def set_address(self, address):
        self.driver.find_element(*OrderFirstPageLocators.ADDRESS_FIELD).send_keys(address)

    def set_phone(self, phone):
        self.driver.find_element(*OrderFirstPageLocators.PHONE_FIELD).send_keys(phone)  
    
    def click_next_button(self):
        self.driver.find_element(*OrderFirstPageLocators.BUTTON_NEXT).click()

    def set_metro(self, metro):
        self.driver.find_element(*OrderFirstPageLocators.METRO_FIELD).click()
        self.driver.find_element(*OrderFirstPageLocators.METRO_FIELD).send_keys(metro)
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, f"//div[contains(@class,'select-search__select')]//div[text()='{metro}']")
        )
    ).click()
        