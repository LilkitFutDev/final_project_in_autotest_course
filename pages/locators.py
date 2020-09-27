from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
      LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
      REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
      URL = "login"

class FindCart():
    BUTTON_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    SUCCESSFUL_ADDITION = (By.CSS_SELECTOR, ".alertinner strong")
    COST_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main")
    COST_CART = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in")
    NAMED_OF_BOOK = (By.CSS_SELECTOR,"#content_inner .col-sm-6.product_main h1")


