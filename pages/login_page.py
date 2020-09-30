from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        inn = self.browser.current_url
        assert inn.find(LoginPageLocators.URL) > 0

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM)

    def register_new_user(self, email, password):
        email1 = self.browser.find_element(*Register.EMAIL)
        email1.send_keys(email)

        password1 = self.browser.find_element(*Register.PASSWORD)
        password1.send_keys(password)

        repeat_password = self.browser.find_element(*Register.REPEAT_PASSWORD)
        repeat_password.send_keys(password)

        registration_button = self.browser.find_element(*Register.BUTTON_REGISTER)
        registration_button.click()
