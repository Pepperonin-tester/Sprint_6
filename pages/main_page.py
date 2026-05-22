from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_question(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def click_question_button(self, locator):
        self.driver.find_element(*locator).click()
    
    def open(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    def visible_answer_text(self, locator):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.visibility_of_element_located(locator)
    )
        return self.driver.find_element(*locator).text
    
    def click_order_button(self, locator):
        self.driver.find_element(*locator).click()

    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()

    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()