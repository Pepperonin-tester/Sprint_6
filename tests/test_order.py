import pytest
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderConfirmPageLocators
from pages import main_page
from pages.main_page import MainPage
from pages.order_first_page import OrderFirstPage
from pages.order_second_page import OrderSecondPage
from pages.order_confirm_page import OrderConfirmPage

@pytest.mark.parametrize('order_button, name, last_name, address, metro, phone, date, period, color, comment', [
    (MainPageLocators.ORDER_BUTTON_TOP, 'Иван', 'Иванов', 'ул. Ленина 1', 'Черкизовская', '+79991234567', '24.05.2026', 'сутки', 'black', 'Позвоните заранее'),
    (MainPageLocators.ORDER_BUTTON_BOTTOM, 'Петр', 'Петров', 'ул. Мира 5', 'Сокольники', '+79997654321', '25.05.2026', 'двое суток', 'grey', 'Домофон не работает'),
])

def test_order(driver, order_button, name, last_name, address, metro, phone, date, period, color, comment):
    main_page = MainPage(driver)
    main_page.open()
    main_page.accept_cookies()
    main_page.click_order_button(order_button)

    order_first_page = OrderFirstPage(driver)
    order_first_page.set_name(name)
    order_first_page.set_last_name(last_name)
    order_first_page.set_address(address)
    order_first_page.set_metro(metro)
    order_first_page.set_phone(phone)
    order_first_page.click_next_button()

    order_second_page = OrderSecondPage(driver)
    order_second_page.set_date(date)
    order_second_page.set_rental_period(period)
    order_second_page.set_color(color)
    order_second_page.set_comment(comment)
    order_second_page.click_order_button()

    order_confirm_page = OrderConfirmPage(driver)
    order_confirm_page.click_confirm_yes_button()
    success_message = order_confirm_page.get_order_success_message()
    
    assert 'Заказ оформлен' in success_message
