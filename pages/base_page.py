import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        with allure.step(f'Кликнуть на элемент {locator}'):
            self.find_element(locator).click()

    def send_keys_to_element(self, locator, text):
        with allure.step(f'Ввести текст {text} в элемент {locator}'):
            self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        with allure.step(f'Получить текст элемента {locator}'):
            return self.wait_and_find_element(locator).text

    def open(self, url):
        with allure.step(f'Открыть страницу {url}'):
            self.driver.get(url)