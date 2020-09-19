from selenium.webdriver.common.by import By
from .base_page import BasePage



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(BasePage):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"