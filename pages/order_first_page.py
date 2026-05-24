import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.order_page_locators import OrderFirstPageLocators
from pages.base_page import BasePage


class OrderFirstPage(BasePage):
    def set_name(self, name):
        with allure.step(f'Ввести имя {name}'):
            self.send_keys_to_element(OrderFirstPageLocators.NAME_FIELD, name)

    def set_last_name(self, last_name):
        with allure.step(f'Ввести фамилию {last_name}'):
            self.send_keys_to_element(OrderFirstPageLocators.LAST_NAME_FIELD, last_name)

    def set_address(self, address):
        with allure.step(f'Ввести адрес {address}'):
            self.send_keys_to_element(OrderFirstPageLocators.ADDRESS_FIELD, address)

    def set_phone(self, phone):
        with allure.step(f'Ввести телефон {phone}'):
            self.send_keys_to_element(OrderFirstPageLocators.PHONE_FIELD, phone)

    def set_metro(self, metro):
        with allure.step(f'Выбрать станцию метро {metro}'):
            self.click_element(OrderFirstPageLocators.METRO_FIELD)
            self.send_keys_to_element(OrderFirstPageLocators.METRO_FIELD, metro)
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, f"//div[contains(@class,'select-search__select')]//div[text()='{metro}']")
                )
            ).click()

    def click_next_button(self):
        with allure.step('Нажать кнопку Далее'):
            self.click_element(OrderFirstPageLocators.BUTTON_NEXT)
