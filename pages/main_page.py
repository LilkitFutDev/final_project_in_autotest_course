from .base_page import BasePage
from .locators import *

class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK)

    def should_be_login_link(self):
       assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


