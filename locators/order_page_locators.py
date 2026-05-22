from selenium.webdriver.common.by import By

class OrderFirstPageLocators:
    # Поле "Имя"
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    # Поле "Фамилия"
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Поле "Адрес"
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Поле "Станция метро"
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Поле "Телефон"
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее"
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

class OrderSecondPageLocators:
    # Поле "Когда привезти самокат"
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Поле "Срок аренды"
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-control']")
    # Чекбокс "Черный жемчуг"
    COLOR_BLACK = (By.XPATH, "//label[@for='black']")
    # Чекбокс "Серая безысходность"
    COLOR_GREY = (By.XPATH, "//label[@for='grey']")
    # Поле "Комментарий для курьера"
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка "Заказать"
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")

class OrderConfirmPageLocators:
    # Кнопка "Да" в окне подтверждения заказа
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']//button[text()='Да']")
    # Сообщение об успешном заказе
    ORDER_SUCCESS_HEADER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")