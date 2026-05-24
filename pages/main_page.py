import allure
import time
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def open(self):
        with allure.step('Открыть главную страницу'):
            self.driver.get('https://qa-scooter.praktikum-services.ru/')

    def accept_cookies(self):
        with allure.step('Принять куки'):
            self.click_element(MainPageLocators.COOKIE_BUTTON)

    def scroll_to_question(self, locator):
        with allure.step('Проскроллить до вопроса'):
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(1)

    def click_question_button(self, locator):
        with allure.step('Кликнуть на вопрос'):
            self.click_element(locator)

    def visible_answer_text(self, locator):
        with allure.step('Получить текст ответа'):
            return self.get_text(locator)

    def click_order_button(self, locator):
        with allure.step('Кликнуть на кнопку Заказать'):
            self.click_element(locator)

    def click_scooter_logo(self):
        with allure.step('Кликнуть на логотип Самоката'):
            self.click_element(MainPageLocators.LOGO_SCOOTER)

    def click_yandex_logo(self):
        with allure.step('Кликнуть на логотип Яндекса'):
            self.click_element(MainPageLocators.LOGO_YANDEX)
            