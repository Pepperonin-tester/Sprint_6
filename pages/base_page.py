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

    def scroll_to_element(self, locator):
        with allure.step(f'Проскроллить до элемента {locator}'):
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(locator)
        )

    def wait_for_new_window(self):
        with allure.step('Ожидать открытия новой вкладки'):
            WebDriverWait(self.driver, 10).until(
                expected_conditions.number_of_windows_to_be(2)
            )

    def switch_to_new_window(self):
        with allure.step('Переключиться на новую вкладку'):
            self.wait_for_new_window()
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
            WebDriverWait(self.driver, 10).until(
                expected_conditions.url_contains('dzen.ru')
        )

    def wait_and_find_element_by_xpath(self, xpath):
        with allure.step(f'Ожидать элемент по xpath {xpath}'):
            return WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(
                    ('xpath', xpath)
                )
            )
        
    def get_current_url(self):
        with allure.step('Получить текущий URL'):
            return self.driver.current_url
        