import time
from pages.main_page import MainPage


class TestRedirects:
    def test_redirect_to_scooter_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_scooter_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def test_redirect_to_yandex_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        time.sleep(3)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        assert 'dzen.ru' in driver.current_url
        