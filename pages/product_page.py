from .base_page import BasePage
from .locators import *


class CartPage(BasePage):

    def can_click_product_to_basket(self):
        cart_button = self.browser.find_element(*FindCart.BUTTON_CART)
        cart_button.click()
        self.solve_quiz_and_get_code()

    def can_click_product_to_basket_without_solve(self):
        cart_button = self.browser.find_element(*FindCart.BUTTON_CART)
        cart_button.click()

    def assert_on_true_that_book_in_cart(self):
        succ = self.browser.find_element(*FindCart.SUCCESSFUL_ADDITION)
        named_book = self.browser.find_element(*FindCart.NAMED_OF_BOOK)
        assert succ.text == named_book.text, "assert_on_true_that_book_in_cart - fall here"

    def assert_value_cart(self):
        cost = self.browser.find_element(*FindCart.COST_CART)
        up = self.browser.find_element(*FindCart.COST_PRODUCT)
        assert cost.text.find(up.text), "assert_value_cart - fall here"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*FindCart.SUCCESSFUL_ADDITION), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_with_disappeared(self):
        assert self.is_disappeared(*FindCart.SUCCESSFUL_ADDITION), \
            "Success message is presented, but should not be"
