from pages.main_page import MainPage


class TestRedirects:
    def test_redirect_to_scooter_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/'

    def test_redirect_to_yandex_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        assert 'dzen.ru' in main_page.get_current_url()
