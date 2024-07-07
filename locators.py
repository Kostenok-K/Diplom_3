from selenium.webdriver.common.by import By


class MainPage:
    ACCOUNT_LINK = [By.XPATH, "//header//a[@href='/account']"]
    CONSTRUCTOR_LINK = [By.XPATH, "//nav//a[contains(@class, 'AppHeader') and @href='/']"]
    ORDER_FEED = [By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']"]
    ORDER_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']"]
    BUN_INGREDIENT = [By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']"]
    SAUCE_INGREDIENT = [By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa74']"]
    TOPPING_INGREDIENT = [By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa78']"]
    DETAILS = [By.XPATH, ".//h2[@class= 'Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m "
                         "text text_type_main-large pl-10']"]
    CLOSE = [By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    POPUP = [By.XPATH, ".//div[@class = 'Modal_modal__contentBox__sCy8X pt-10 pb-15']"]
    MY_BURGER = [By.XPATH, "//span[@class = 'constructor-element__row']"]
    ORDER_PLACED = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p[text()='идентификатор заказа']"]
    INGREDIENT_COUNTER = [By.XPATH,
                          ".//a[contains(@class, 'BurgerIngredient_ingredient_')]//p[contains(@class, 'counter_counter__num')]"]


class LoginPage:
    EMAIL_FIELD = [By.XPATH, "//form//label[text() = 'Email']/../input"]
    PASSWORD_FIELD = [By.XPATH, "//form//input[@type='password']"]
    LOGIN_BUTTON = [By.XPATH, "//form//button"]
    RESTORE_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")


class AccountPage:
    PROFILE_IN_ACCOUNT = [By.XPATH, ".//a[@href='/account/profile' and text()='Профиль']"]
    ORDERS_HISTORY = [By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']"]
    ORDER_HISTORY_INACTIVE = [By.XPATH,
                              "//a[@class = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive']"]
    ORDER_HISTORY_ACTIVE = [By.XPATH,
                            ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"]
    EXIT_BUTTON = [By.XPATH, ".//button[contains(@class, 'Account_button')][text()='Выход']"]


class OrderFeed:
    ORDER = [By.XPATH, "//li[@class = 'OrderHistory_listItem__2x95r mb-6'][1]"]
    NUMBER_ORDER_FROM_FEED = [By.XPATH, "//p[@class = 'text text_type_digits-default mb-10 mt-5']"]
    CONTAIN = [By.XPATH, "//p[@class = 'text text_type_main-medium mb-8']"]
    CONTAINING_ELEMENTS = [By.XPATH, "//p[@class = 'undefined text text_type_main-default'][1]"]
    STATUS = [By.XPATH, "//p[@class = 'undefined text text_type_main-default mb-15']"]
    ORDER_IN_ORDER_FEED = [By.XPATH, "//p[@class='text text_type_digits-default']"]
    COMPLETED_ORDERS_TODAY_BEFORE = [By.XPATH, ".//div/p[text()='Выполнено за сегодня:']/following-sibling::p"]
    LABEL_ALL_ORDERS_ARE_READY = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]"
                                            "/li[text()='Все текущие заказы готовы!']"]
    ORDER_LIST = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='{}']"]


class RestorePage:
    RESTORE_PASSWORD_TEXT = [By.XPATH, "//h2[text()='Восстановление пароля']"]
    RESTORE_EMAIL_FIELD = [By.XPATH, '//input[@class="text input__textfield text_type_main-default"]']
    RESTORE_BUTTON = [By.XPATH, "//form//button[text()= 'Восстановить']"]
    CODE_INPUT = [By.XPATH, '//*[@class="input pr-6 pl-6 input_type_text input_size_default"]']
    RESTORE_PASSWORD_ACTIVE_INPUT = [By.XPATH,
                                     './/div[@class="input pr-6 pl-6 input_type_text input_size_default '
                                     'input_status_active"]']
    EYE = [By.XPATH, './/div[@class = "input__icon input__icon-action"]']
