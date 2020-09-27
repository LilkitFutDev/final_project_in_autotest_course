
from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import *
import time
import math


class CartPage(BasePage):


    def can_click_product_to_basket(self):
        cart_button = self.browser.find_element(*FindCart.BUTTON_CART)
        cart_button.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        time.sleep(3)

    def assert_on_true_that_book_in_cart(self):
        succ = self.browser.find_element(*FindCart.SUCCESSFUL_ADDITION)
        named_book = self.browser.find_element(*FindCart.NAMED_OF_BOOK)
        print(succ.text)
        print(named_book.text)
        assert succ.text == named_book.text, "assert_on_true_that_book_in_cart - fall here"

    def assert_value_cart(self):
        cost = self.browser.find_element(*FindCart.COST_CART)
        up = self.browser.find_element(*FindCart.COST_PRODUCT)
        assert cost.text.find(up.text), "assert_value_cart - fall here"








