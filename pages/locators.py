from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, "#logout_link")  # Делаю задание и залипаю, чтоб не тратить время сделаю
    # проверку по кнопке Logout ведь если пользователь
    # не залогинен ее и не будет


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class FindCart():
    BUTTON_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    SUCCESSFUL_ADDITION = (By.CSS_SELECTOR, ".alertinner strong")
    COST_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main")
    COST_CART = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in")
    NAMED_OF_BOOK = (By.CSS_SELECTOR, "#content_inner .col-sm-6.product_main h1")


class Basket():
    BASKET = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_NULL = (By.CSS_SELECTOR, "#content_inner")


class Register():
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[name = 'registration_submit'")
